#include <iostream>

#include "ast.hh"
#include "builtins.hh"

namespace typhon {
namespace ast {

TypedExpression *TypedExpression::evaluate(Context *ctx) { return static_cast<TypedExpression *>(this); }

IntegerLiteralExpression::IntegerLiteralExpression(int _n) { n = _n; }

type::Type *IntegerLiteralExpression::type(Context *ctx) { return &Prim_Int32; }

TypedExpression *IntegerLiteralExpression::evaluate(Context *ctx) { return this; }

VariableExpression::VariableExpression(std::string _name) { name = _name; }

type::Type *VariableExpression::type(Context *ctx) { return ctx->type(name); }

TypedExpression *VariableExpression::evaluate(Context *ctx) { return ctx->load(name); }

BinaryOperationExpression::BinaryOperationExpression(Expression *_left, enum BINOP _op, Expression *_right) : left(_left), op(_op), right(_right) {}

TypedExpression *BinaryOperationExpression::typecheck(Context *ctx) {
    TypedExpression *t_left = left->typecheck(ctx), *t_right = right->typecheck(ctx);

    // hardcode this for now
    if (op == O_PLUS) {
        if (!(t_left->type(ctx) == &Prim_Int32 && t_right->type(ctx) == &Prim_Int32))
            throw new TypeError();
        return new TypedBinaryOperationExpression(&Prim_Int32, t_left, op, t_right);
    }
    return t_left;
}

TypedBinaryOperationExpression::TypedBinaryOperationExpression(type::Type *type, Expression *_left, enum BINOP _op, Expression *_right)
    : BinaryOperationExpression(_left, _op, _right), _type(type) {}

type::Type *TypedBinaryOperationExpression::type(Context *ctx) { return _type; }

AssignStatement::AssignStatement(std::string _name, Expression *_expr) {
    // TODO: figure out type of expr here
    name = _name;
    expr = _expr;
}

AssignStatement::~AssignStatement() {}

void AssignStatement::evaluate(Context *ctx) {
    TypedExpression *value = expr->typecheck(ctx)->evaluate(ctx);
    ctx->store(name, value);
}

ReassignStatement::ReassignStatement() {}

ReassignStatement::~ReassignStatement() {}

ExpressionStatement::ExpressionStatement(Expression *_expr) : expr(_expr) {}

void ExpressionStatement::evaluate(Context *ctx) { std::cout << "expression" << std::endl; }

ExpressionStatement::~ExpressionStatement() {}

FuncDefStatement::FuncDefStatement(std::string _name) : name(_name) {}

void FuncDefStatement::evaluate(Context *ctx) { std::cout << "statement:" << name << std::endl; }

FuncDefStatement::~FuncDefStatement() {}

} // namespace ast
} // namespace typhon
