#include <iostream>

#include "ast.hh"

namespace typhon {
namespace ast {

TypedExpression *Expression::evaluate(class Context *ctx) {
    return new TypedExpression();
}

IntegerLiteralExpression::IntegerLiteralExpression(int _n) { n = _n; }

AssignStatement::AssignStatement(std::string _name, class Expression *_expr) {
    // TODO: figure out type of expr here
    name = _name;
    expr = _expr;
}

AssignStatement::~AssignStatement() {}

void AssignStatement::evaluate(class Context *ctx) {
    ctx->store(name, static_cast<class TypedExpression *>(expr));
}

ReassignStatement::ReassignStatement() {}

ReassignStatement::~ReassignStatement() {}

ExpressionStatement::ExpressionStatement(class Expression *_expr)
    : expr(_expr) {}

void ExpressionStatement::evaluate(class Context *ctx) {
    std::cout << "expression" << std::endl;
}

ExpressionStatement::~ExpressionStatement() {}

FuncDefStatement::FuncDefStatement(std::string _name) : name(_name) {}

void FuncDefStatement::evaluate(class Context *ctx) {
    std::cout << "statement:" << name << std::endl;
}

FuncDefStatement::~FuncDefStatement() {}

} // namespace ast
} // namespace typhon
