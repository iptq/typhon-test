use hir;
use types::{Literal, Type};

#[derive(Debug)]
pub enum Expr {
    Literal(Literal),
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

impl Expr {
    pub fn convert(&self) -> hir::Expr {
        let (kind, ty) = match self {
            &Expr::Literal(ref v) => (hir::ExprKind::Literal(&v), v.ty()),
        };
        hir::Expr { kind, ty }
    }
}

impl<'input> Stmt<'input> {
    pub fn convert(&self) -> hir::Stmt {
        match self {
            &Stmt::Expr(ref expr) => {
                let expr = expr.convert();
                let ty = expr.ty.clone();
                hir::Stmt {
                    kind: hir::StmtKind::Expr(expr),
                    ty,
                }
            }
            _ => hir::Stmt {
                kind: hir::StmtKind::Function,
                ty: Type::Unimplemented,
            },
        }
    }
}

impl<'input> Program<'input> {
    pub fn convert(&self) -> hir::Program {
        let mut functions = Vec::new();
        for stmt in &self.stmts {
            match stmt {
                &Stmt::FuncDef { ref name, ref body } => functions.push(hir::Stmt {
                    kind: hir::StmtKind::Function,
                    ty: Type::Unimplemented,
                }),
                _ => panic!("regular statements shouldn't occur in top level."),
            }
        }
        return hir::Program { functions };
    }
}
