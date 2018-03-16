#include <iostream>

#include "ast.hh"
#include "builtins.hh"

namespace typhon {
namespace ast {

TypedExpression *TypedExpression::evaluate(Context *ctx) { return this; }

IntegerLiteralExpression::IntegerLiteralExpression(int _n) : n(_n) {}

type::Type *IntegerLiteralExpression::type(Context *ctx) { return &Prim_Int32; }

CharacterLiteralExpression::CharacterLiteralExpression(char _c) : c(_c) {}

type::Type *CharacterLiteralExpression::type(Context *ctx) { return &Prim_Char; }

VariableExpression::VariableExpression(std::string _name) : name(_name) {}

type::Type *VariableExpression::type(Context *ctx) { return ctx->type(name); }

TypedExpression *VariableExpression::evaluate(Context *ctx) { return ctx->load(name); }

BinaryOperationExpression::BinaryOperationExpression(Expression *_left, enum BINOP _op, Expression *_right) : left(_left), op(_op), right(_right) {}

TypedExpression *BinaryOperationExpression::typecheck(Context *ctx) {
    TypedExpression *t_left = left->typecheck(ctx), *t_right = right->typecheck(ctx);

    // hardcode this for now
    if (op == O_PLUS) {
        if (!(t_left->type(ctx) == &Prim_Int32 and t_right->type(ctx) == &Prim_Int32))
            throw TypeError();
        return new TypedBinaryOperationExpression(&Prim_Int32, t_left->typecheck(ctx), op, t_right->typecheck(ctx));
    }
    return t_left;
}

TypedBinaryOperationExpression::TypedBinaryOperationExpression(type::Type *type, TypedExpression *_left, enum BINOP _op, TypedExpression *_right)
    : BinaryOperationExpression(_left, _op, _right), left(_left), op(_op), right(_right), _type(type) {}

type::Type *TypedBinaryOperationExpression::type(Context *ctx) { return _type; }

TypedExpression *TypedBinaryOperationExpression::evaluate(Context *ctx) {
    // hardcode this for now
    if (op == O_PLUS) {
        if (!(left->type(ctx) == &Prim_Int32 and right->type(ctx) == &Prim_Int32))
            throw TypeError();
        return new IntegerLiteralExpression(dynamic_cast<IntegerLiteralExpression *>(left->evaluate(ctx))->n +
                                            dynamic_cast<IntegerLiteralExpression *>(right->evaluate(ctx))->n);
    }
    return this;
}

mir::Node *Block::convert() { return new mir::Node(); }

AssignStatement::AssignStatement(std::string _name, Expression *_expr) : name(_name), expr(_expr) {}

void AssignStatement::evaluate(Context *ctx) {
    TypedExpression *value = expr->typecheck(ctx)->evaluate(ctx);
    ctx->store(name, value);
}

ReassignStatement::ReassignStatement() {}

ReassignStatement::~ReassignStatement() {}

ExpressionStatement::ExpressionStatement(Expression *_expr) : expr(_expr) {}

void ExpressionStatement::evaluate(Context *ctx) {}

FuncDefStatement::FuncDefStatement(std::string _name) : name(_name) {}

void FuncDefStatement::evaluate(Context *ctx) { std::cout << "statement:" << name << std::endl; }

} // namespace ast
} // namespace typhon
