extern crate clap;
extern crate typhon;

use std::fs::File;
use std::io::prelude::*;

use clap::{App, Arg};

use typhon::lexer::Lexer;
use typhon::parser::parse_Program;

fn main() {
    let matches = App::new("Typhon")
        .version("0.1")
        .author("Michael Zhang <failed.down@gmail.com>")
        .about("Statically typed language with Python syntax.")
        .arg(
            Arg::with_name("file")
                .help("The file to compile.")
                .required(true)
                .index(1),
        )
        .get_matches();

    // unwrapping cuz required(true)
    let filename = matches.value_of("file").unwrap();

    let mut f = File::open(filename).expect("file not found");

    let mut contents = String::new();
    f.read_to_string(&mut contents).expect("failed to read");
    contents += "\n";

    // parsing
    let lexer = Lexer::new(&contents);
    let program = parse_Program(lexer);
    println!("program: {:?}", program);
}
