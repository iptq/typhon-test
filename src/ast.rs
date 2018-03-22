use lexer::{Number, Token};

#[derive(Debug)]
pub enum Expr<'input> {
    IntLiteral(i32),
    UIntLiteral(u32),
    Number(Number),
    fuck(Token<'input>),
}

#[derive(Debug)]
pub enum Stmt<'input> {
    Expr(Expr<'input>),
    FuncDef(&'input str, Vec<Stmt<'input>>),
    Return(Expr<'input>),
}

#[derive(Debug)]
pub struct Program;
