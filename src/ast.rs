pub enum Expr {
    IntLiteral(i32),
    UIntLiteral(u32),
}

pub enum Stmt {
    Expr(Expr),
    FuncDef,
}

pub struct Program;
