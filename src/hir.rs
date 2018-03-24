use types::{Literal, Type};

#[derive(Debug)]
pub enum ExprKind<'input> {
    Literal(&'input Literal),
}

#[derive(Debug)]
pub struct Expr<'input> {
    pub ty: Type,
    pub kind: ExprKind<'input>,
}

#[derive(Debug)]
pub enum StmtKind<'input> {
    Expr(Expr<'input>),
    Function,
}

#[derive(Debug)]
pub struct Stmt<'input> {
    pub kind: StmtKind<'input>,
    pub ty: Type,
}

#[derive(Debug)]
pub struct Program<'input> {
    pub functions: Vec<Stmt<'input>>,
}
