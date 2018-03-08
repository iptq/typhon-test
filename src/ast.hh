#ifndef SRC_AST_H_
#define SRC_AST_H_

#include <string>

#include "context.hh"

namespace typhon {
namespace ast {

class Expression {};

class Statement {
  public:
    virtual void evaluate(class Context &ctx) {}
};

class FuncDef : public Statement {
  public:
    FuncDef(std::string _name);
    virtual ~FuncDef();
    std::string name;
    virtual void evaluate(class Context &ctx);
};

} // namespace ast
} // namespace typhon

#endif