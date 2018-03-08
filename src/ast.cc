#include <iostream>

#include "ast.hh"

namespace typhon {
namespace ast {

TypedExpression *Expression::evaluate(Context *ctx) {
    return static_cast<TypedExpression *>(this);
}

IntegerLiteralExpression::IntegerLiteralExpression(int _n) { n = _n; }

TypedExpression *IntegerLiteralExpression::evaluate(Context *ctx) {
    return this;
}

VariableExpression::VariableExpression(std::string _name) { name = _name; }

TypedExpression *VariableExpression::evaluate(Context *ctx) {
    return ctx->load(name);
}

AssignStatement::AssignStatement(std::string _name, Expression *_expr) {
    // TODO: figure out type of expr here
    name = _name;
    expr = _expr;
}

AssignStatement::~AssignStatement() {}

void AssignStatement::evaluate(Context *ctx) {
    TypedExpression *value = expr->evaluate(ctx);
    ctx->store(name, value);
}

ReassignStatement::ReassignStatement() {}

ReassignStatement::~ReassignStatement() {}

ExpressionStatement::ExpressionStatement(Expression *_expr) : expr(_expr) {}

void ExpressionStatement::evaluate(Context *ctx) {
    std::cout << "expression" << std::endl;
}

ExpressionStatement::~ExpressionStatement() {}

FuncDefStatement::FuncDefStatement(std::string _name) : name(_name) {}

void FuncDefStatement::evaluate(Context *ctx) {
    std::cout << "statement:" << name << std::endl;
}

FuncDefStatement::~FuncDefStatement() {}

} // namespace ast
} // namespace typhon
