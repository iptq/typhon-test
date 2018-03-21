#[derive(Debug)]
pub enum Expr {
    IntLiteral(i32),
    UIntLiteral(u32),
}

#[derive(Debug)]
pub enum Stmt {
    Expr(Expr),
    FuncDef,
}

#[derive(Debug)]
pub struct Program;
