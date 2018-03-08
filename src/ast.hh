#ifndef SRC_AST_H_
#define SRC_AST_H_

#include <string>

#include "context.hh"
#include "types.hh"

namespace typhon {
namespace ast {

class Expression {};

class TypedExpression : public Expression {
  public:
    class Type *type;
};

class Statement {
  public:
    virtual void evaluate(class Context &ctx) {}
};

class AssignStatement : public Statement {
  public:
    AssignStatement();
    virtual ~AssignStatement();
};

class ReassignStatement : public Statement {
  public:
    ReassignStatement();
    virtual ~ReassignStatement();
};

class ExpressionStatement : public Statement {
  public:
    ExpressionStatement(class Expression *_expr);
    virtual ~ExpressionStatement();
    virtual void evaluate(class Context &ctx);

    class Expression *expr;
};

class FuncDefStatement : public Statement {
  public:
    FuncDefStatement(std::string _name);
    virtual ~FuncDefStatement();
    virtual void evaluate(class Context &ctx);

    std::string name;
};

} // namespace ast
} // namespace typhon

#endif