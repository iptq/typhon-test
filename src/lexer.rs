use std::str::CharIndices;
use std::iter::Peekable;

pub type Spanned<Token, Location, Error> = Result<(Location, Token, Location), Error>;

#[derive(Debug)]
pub enum Token {
}

#[derive(Debug)]
pub enum LexError {
}

pub struct Lexer<'input> {
    chars: Peekable<CharIndices<'input>>,
    queue: Vec<Spanned<Token, usize, LexError>>,
}

impl<'input> Lexer<'input> {
    pub fn new(input: &'input str) -> Self {
        Lexer {
            chars: input.char_indices().peekable(),
            queue: Vec::new(),
        }
    }
}

impl<'input> Iterator for Lexer<'input> {
    type Item = Spanned<Token, usize, LexError>;
    fn next(&mut self) -> Option<Self::Item> {
        self.chars.next();
        if !self.queue.is_empty() {
            return self.queue.pop();
        }
        None
    }
}
