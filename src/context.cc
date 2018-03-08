#include "context.hh"
#include "ast.hh"

namespace typhon {

void Context::store(std::string key, class ast::TypedExpression *expr) {
    ast::TypedExpression value = *expr;
    globals.insert(
        std::pair<std::string, class ast::TypedExpression>(key, value));
}

} // namespace typhon