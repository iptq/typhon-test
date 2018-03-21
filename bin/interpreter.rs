extern crate linefeed;
extern crate typhon;

use linefeed::{ReadResult, Reader};

use typhon::lexer::Lexer;
use typhon::parser::parse_Line;

fn main() {
    let mut reader;

    match Reader::new(":b") {
        Ok(anything) => reader = anything,
        Err(error) => panic!("{}", error),
    }
    reader.set_prompt(">>> ");

    while let Ok(ReadResult::Input(line)) = reader.read_line() {
        let trimmed = line.trim();
        if !trimmed.is_empty() {
            reader.add_history(line.clone());
        }

        let mut lexer = Lexer::new(&trimmed);
        for token in lexer {
            println!("token: {:?}", token);
        }
        let mut lexer = Lexer::new(&trimmed);
        let stmt = parse_Line(lexer);
        println!("{:?}", stmt);
    }
}