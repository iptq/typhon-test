use std::collections::VecDeque;
use std::str::FromStr;

const TAB_INDENT_WIDTH: usize = 8;
const MAX_DEPTH: usize = 64;

pub type Spanned<Token, Location, Error> = Result<(Location, Token, Location), Error>;

#[derive(Debug)]
pub enum Number {
    Integer(i32),
    UInteger(u32),
    LongInteger(i64),
    ULongInteger(u64),
    Float(f32),
    LongFloat(f64),
}

#[derive(Debug)]
pub enum Token<'input> {
    // indentation
    Newline,
    Indent,
    Dedent,
    EOF,

    // symbols
    LeftParen,
    RightParen,
    Colon,

    // literals
    Number(Number),

    String,
    Symbol(&'input str),
    Ident,
    Digit,
    Char,
}

#[derive(Debug)]
pub struct LexError {
    message: String,
}

pub struct Lexer<'input> {
    source: &'input str,
    position: usize,
    queue: VecDeque<Spanned<Token<'input>, usize, LexError>>,
    istack: Vec<usize>,
    nesting: usize,
    first: bool,
}

impl<'input> Lexer<'input> {
    pub fn new(input: &'input str) -> Self {
        let mut lexer = Lexer {
            source: input,
            position: 0,
            queue: VecDeque::new(),
            istack: vec![0],
            nesting: 0,
            first: true,
        };
        lexer.precalc();
        lexer
    }
    fn rest(&self) -> &'input str {
        return &self.source[self.position..];
    }
    fn peek(&self, offset: usize) -> Option<char> {
        let rest = self.rest();
        if rest.len() == 0 {
            return None;
        }
        return rest.chars().nth(offset);
    }
    fn peekwhile<F>(&self, f: F, offset: usize) -> &'input str
    where
        F: Fn(char) -> bool,
    {
        let mut length: usize = offset;
        while let Some(ch) = self.peek(length) {
            if !f(ch) {
                break;
            }
            length += 1;
        }
        return &self.rest()[offset..length];
    }
    fn whitecount(&self, line: &'input str) -> (usize, usize) {
        let mut count = 0usize;
        let mut len = 0usize;
        for c in line.chars() {
            if !(c == '\t' || c == ' ') {
                break;
            }
            count += 1;
            len += match c {
                '\t' => TAB_INDENT_WIDTH,
                ' ' => 1,
                _ => 0,
            };
        }
        return (len, count);
    }
    fn indentcalc(&mut self, line: &'input str) -> usize {
        if self.nesting > 0 {
            return 0;
        }

        let (whitelen, whitecount) = self.whitecount(line);
        // println!("whitelen: {}, stack: {:?}", whitelen, self.istack);
        let mut level = self.istack.len() - 1;
        if whitelen == self.istack[level] {
            if !self.first {
                self.queue
                    .push_back(Ok((self.position, Token::Newline, self.position + 1)));
            }
            self.first = false;
            return 0;
        }

        if whitelen > self.istack[level] {
            self.queue.push_back(Ok((
                self.position,
                Token::Indent,
                self.position + whitecount,
            )));
            if level + 1 > MAX_DEPTH {
                panic!("exceeded max depth");
            }
            self.istack.push(whitelen);
            return whitelen;
        }

        while whitelen < self.istack[level] {
            level -= 1;
            self.queue
                .push_back(Ok((self.position, Token::Dedent, self.position)));
            self.istack.pop();
        }

        0
    }
    fn read_ident(&mut self) {
        // already guaranteed that ch is not going to be a digit
        let name = self.peekwhile(
            |ch| {
                (ch >= 'a' && ch <= 'z') || (ch >= 'A' && ch <= 'Z') || (ch >= '0' && ch <= '9')
                    || ch == '_'
            },
            0,
        );
        let length = name.len();
        self.queue
            .push_back(Ok((self.position, Token::Ident, self.position + length)));
        self.position += length;
    }
    fn read_number_generic(&self, base: u32) -> Option<(Number, usize)> {
        let mut dstr = String::new();
        let mut length = 0;
        let mut float = false;
        let mut unsigned = false;
        let mut long = false;
        let mut dchecked = false;
        let mut uchecked = false;
        let mut lchecked = false;
        if base != 10 {
            length += 2;
        }
        while let Some(c) = self.peek(length) {
            match c {
                '0'...'9' => if lchecked || uchecked {
                    return None;
                } else {
                    dstr += &c.to_string();
                },
                'a'...'f' | 'A'...'F' => if lchecked || uchecked {
                    return None;
                } else if base == 16 {
                    dstr += &c.to_string();
                },
                '.' => if lchecked || uchecked {
                    return None;
                } else {
                    float = true;
                    dstr += &c.to_string();
                },
                'u' => if lchecked || float {
                    return None; // this is definitely an error
                } else {
                    unsigned = true;
                    uchecked = true;
                },
                'L' => {
                    long = true;
                    lchecked = true;
                }
                _ => break,
            }
            length += 1;
        }
        println!(
            "shiet {:?} (float={}, long={}, unsigned={})",
            dstr, float, long, unsigned
        );
        // temporarily using unwrap here, we know what chars are in this string anyway
        Some((
            if float {
                if long {
                    Number::LongFloat(FromStr::from_str(&dstr).unwrap())
                } else {
                    Number::Float(FromStr::from_str(&dstr).unwrap())
                }
            } else {
                match (unsigned, long) {
                    (true, true) => Number::ULongInteger(u64::from_str_radix(&dstr, base).unwrap()),
                    (true, false) => Number::UInteger(u32::from_str_radix(&dstr, base).unwrap()),
                    (false, true) => Number::LongInteger(i64::from_str_radix(&dstr, base).unwrap()),
                    (false, false) => Number::Integer(i32::from_str_radix(&dstr, base).unwrap()),
                }
            },
            length,
        ))
        // Some((
        //     Number::Integer(i32::from_str_radix(&dstr, base as u32).unwrap()),
        //     length,
        // ))
    }
    fn read_number(&mut self) {
        let value = match self.peek(0) {
            Some('0') => match self.peek(1) {
                // this could be bin / oct / hex
                Some('b') | Some('B') => self.read_number_generic(2),
                Some('o') | Some('O') => self.read_number_generic(8),
                Some('x') | Some('X') => self.read_number_generic(16),
                _ => self.read_number_generic(10),
            },
            Some(d) => self.read_number_generic(10),
            None => panic!("invalid"),
        };

        match value {
            Some((v, len)) => {
                self.queue
                    .push_back(Ok((self.position, Token::Number(v), self.position + len)));
                self.position += len;
            }
            None => (),
        }
    }
    fn read_string(&mut self) {
        // TODO: check triple string
        let quote_type: char = self.peek(0).unwrap();
        let mut length = 0;
        while let Some(c) = self.peek(0) {
            // Some(c) => quote_type = c,
            // _ => {
            //     return Err(ParseError {
            //         message: format!("Unexpected parse error."),
            //     });
            // }
            if c == quote_type {
                break;
            }
            length += 1;
        }
        self.queue
            .push_back(Ok((self.position, Token::String, self.position + length)));
        self.position += length + 1; // for quote
    }
    fn skipwhite(&self) -> usize {
        let mut offset = 0;
        loop {
            match self.peek(offset) {
                Some(' ') | Some('\t') => offset += 1,
                _ => break,
            }
        }
        return offset;
    }
    fn precalc(&mut self) {
        while let Some(c) = self.peek(0) {
            if c == '\n' {
                self.queue
                    .push_back(Ok((self.position, Token::Newline, self.position)));
                self.position += 1;
                let chars = self.peekwhile(|c| c != '\n', 0);
                let white = self.indentcalc(chars);
                self.position += white;
                continue;
            } else {
                let white = self.skipwhite();
                self.position += white;
                if white > 0 {
                    continue;
                }
            }

            // check tokens
            if let Some(_c2) = self.peek(1) {
                // match double token
            }
            match c {
                '(' | ')' | '=' | ':' | ';' | '.' | ',' | '+' | '-' | '*' | '/' => {
                    self.queue.push_back(Ok((
                        self.position,
                        Token::Symbol(&self.source[self.position..self.position + 1]),
                        self.position + 1,
                    )));
                    self.position += 1;
                }
                '\'' | '"' => self.read_string(),
                'a'...'z' | 'A'...'Z' => self.read_ident(),
                '0'...'9' => self.read_number(),
                _ => self.position += 1,
            };
        }
        self.queue
            .push_back(Ok((self.position, Token::EOF, self.position)));
    }
}

impl<'input> Iterator for Lexer<'input> {
    type Item = Spanned<Token<'input>, usize, LexError>;
    fn next(&mut self) -> Option<Self::Item> {
        let opt = self.queue.pop_front();
        // match &opt {
        //     &Some(ref tok) => match tok {
        //         &Ok((ref a, ref b, ref c)) => println!(
        //             "{:?}: {:?} ({})",
        //             b,
        //             &self.source[*a..*c],
        //             &self.source[*a..*c].len()
        //         ),
        //         _ => (),
        //     },
        //     _ => (),
        // }
        opt
    }
}
