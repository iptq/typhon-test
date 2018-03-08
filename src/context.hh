#ifndef SRC_CONTEXT_H_
#define SRC_CONTEXT_H_

#include <map>

#include "ast.hh"

namespace typhon {

namespace ast {
class TypedExpression;
}

class Context {
  public:
    void store(std::string key, class ast::TypedExpression *value);

    std::map<std::string, class ast::TypedExpression> globals;
};

} // namespace typhon

#endif