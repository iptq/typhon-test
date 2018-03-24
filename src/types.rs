#[derive(Debug)]
pub enum Type {
    Int,
    Char,
    Float,

    // combinations of types
    Sum(Vec<Type>),
    Prod(Vec<Type>),
}
