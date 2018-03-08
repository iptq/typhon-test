#include <iostream>

#include "ast.hh"

namespace typhon {
namespace ast {

FuncDef::FuncDef(std::string _name) : name(_name) {}

FuncDef::~FuncDef() {}

void FuncDef::evaluate(class Context &ctx) {
    std::cout << "statement" << std::endl;
}

} // namespace ast
} // namespace typhon
