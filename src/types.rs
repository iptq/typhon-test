use lexer::Number;

#[derive(Debug)]
pub enum Literal {
    Int(i32),
    UInt(u32),
    LInt(i64),
    ULInt(u64),
    Float(f32),
    LFloat(f64),
    Char(char),
}

#[derive(Clone, Debug)]
pub enum Type {
    Unimplemented,

    Int,
    UInt,
    LInt,
    ULInt,
    Float,
    LFloat,
    Char,

    // combinations of types
    Sum(Vec<Type>),
    Prod(Vec<Type>),
}

impl Literal {
    pub fn from(number: Number) -> Literal {
        match number {
            Number::Integer(n) => Literal::Int(n),
            Number::UInteger(n) => Literal::UInt(n),
            Number::LongInteger(n) => Literal::LInt(n),
            Number::ULongInteger(n) => Literal::ULInt(n),
            Number::Float(n) => Literal::Float(n),
            Number::LongFloat(n) => Literal::LFloat(n),
        }
    }
    pub fn ty(&self) -> Type {
        match self {
            &Literal::Int(_) => Type::Int,
            &Literal::UInt(_) => Type::UInt,
            &Literal::LInt(_) => Type::LInt,
            &Literal::ULInt(_) => Type::ULInt,
            &Literal::Float(_) => Type::Float,
            &Literal::LFloat(_) => Type::LFloat,
            &Literal::Char(_) => Type::Char,
        }
    }
}
