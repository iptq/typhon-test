#include <iostream>

#include "ast.hh"
#include "context.hh"
#include "exceptions.hh"

namespace typhon {

void Context::store(std::string key, ast::TypedExpression *expr) {
    if (globals.find(key) != globals.end())
        globals.erase(key);

    globals.insert(std::pair<std::string, ast::TypedExpression *>(key, expr));
}

ast::TypedExpression *Context::load(std::string key) {
    auto it = globals.find(key);
    if (it == globals.end())
        throw UnboundVariableError();
    return it->second;
}

type::Type *Context::type(std::string key) { return load(key)->type(this); }

} // namespace typhon