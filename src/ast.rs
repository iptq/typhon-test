use lexer::Number;
use hir;

#[derive(Debug)]
pub enum Value {
    IntLiteral(i32),
    UIntLiteral(u32),
    Number(Number),
}

#[derive(Debug)]
pub enum Expr {
    Value(Value),
}

#[derive(Debug)]
pub enum Stmt<'input> {
    Expr(Expr),
    FuncDef {
        name: &'input str,
        body: Vec<Stmt<'input>>,
    },
    Return(Expr),
}

#[derive(Debug)]
pub struct Program<'input> {
    pub stmts: Vec<Stmt<'input>>,
}

impl<'input> hir::IntoHIR<hir::Stmt> for Stmt<'input> {
    fn convert(&self) -> hir::Stmt {
        match self {
            &Stmt::Expr(ref expr) => hir::Stmt::Function,
            _ => hir::Stmt::Function,
        }
    }
}

impl<'input> hir::IntoHIR<hir::Program> for Program<'input> {
    fn convert(&self) -> hir::Program {
        return hir::Program {
            functions: vec![hir::Stmt::Function],
        };
    }
}
