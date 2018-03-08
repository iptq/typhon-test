#include <iostream>

#include "ast.hh"
#include "context.hh"
#include "exceptions.hh"

namespace typhon {

void Context::store(std::string key, class ast::TypedExpression *expr) {
    ast::TypedExpression value = *expr;

    if (globals.find(key) != globals.end())
        globals.erase(key);

    globals.insert(
        std::pair<std::string, class ast::TypedExpression>(key, value));
    std::cout << "stored" << std::endl;
}

ast::TypedExpression *Context::load(std::string key) {
    auto it = globals.find(key);
    if (it == globals.end())
        throw UnboundVariableException();
    return &it->second;
}

} // namespace typhon