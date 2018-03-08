#ifndef SRC_CONTEXT_H_
#define SRC_CONTEXT_H_

#include <map>

#include "ast.hh"

namespace typhon {

namespace ast {
class TypedExpression; // forward decl
}

class Context {
  public:
    void store(std::string key, ast::TypedExpression *value);
    ast::TypedExpression *load(std::string key);

    std::map<std::string, ast::TypedExpression *> globals;
};

} // namespace typhon

#endif