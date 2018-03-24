use lexer::Number;
use types::Type;

pub trait IntoHIR<T> {
    fn convert(&self) -> T;
}

#[derive(Debug)]
pub enum ExprKind {
    IntLiteral(i32),
    UIntLiteral(u32),
    Number(Number),
}

#[derive(Debug)]
pub struct Expr {
    ty: Type,
    value: ExprKind,
}

#[derive(Debug)]
pub enum Stmt {
    Function,
}

#[derive(Debug)]
pub struct Program {
    pub functions: Vec<Stmt>,
}
