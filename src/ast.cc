#include <iostream>

#include "ast.hh"

namespace typhon {
namespace ast {

AssignStatement::AssignStatement() {}

AssignStatement::~AssignStatement() {}

ReassignStatement::ReassignStatement() {}

ReassignStatement::~ReassignStatement() {}

ExpressionStatement::ExpressionStatement(class Expression *_expr)
    : expr(_expr) {}

void ExpressionStatement::evaluate(class Context &ctx) {
    std::cout << "expression" << std::endl;
}

ExpressionStatement::~ExpressionStatement() {}

FuncDefStatement::FuncDefStatement(std::string _name) : name(_name) {}

void FuncDefStatement::evaluate(class Context &ctx) {
    std::cout << "statement:" << name << std::endl;
}

FuncDefStatement::~FuncDefStatement() {}

} // namespace ast
} // namespace typhon
