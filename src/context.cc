#include <iostream>

#include "ast.hh"
#include "context.hh"

namespace typhon {

void Context::store(std::string key, class ast::TypedExpression *expr) {
    ast::TypedExpression value = *expr;
    globals.insert(
        std::pair<std::string, class ast::TypedExpression>(key, value));
    std::cout << "stored" << std::endl;
}

} // namespace typhon