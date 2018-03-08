#ifndef SRC_AST_H_
#define SRC_AST_H_

#include <string>

#include "context.hh"
#include "exceptions.hh"
#include "types.hh"

namespace typhon {
namespace ast {

class TypedExpression;

class Expression {
  public:
    virtual TypedExpression *evaluate(class Context *ctx);
    virtual std::string to_string() { return "unevaluated expr"; }
};

class TypedExpression : public Expression {
  public:
    class Type *type;
};

class LiteralExpression : public TypedExpression {};

class IntegerLiteralExpression : public LiteralExpression {
  public:
    IntegerLiteralExpression(int _n);
    virtual std::string to_string() { return std::to_string(n); }
    int n;
};

class VariableExpression : public TypedExpression {
  public:
    VariableExpression(std::string _name);
    virtual TypedExpression *evaluate(class Context *ctx);
    std::string name;
};

class Statement {
  public:
    virtual void evaluate(class Context *ctx) {}
};

class AssignStatement : public Statement {
  public:
    AssignStatement(std::string _name, class Expression *_expr);
    virtual ~AssignStatement();
    virtual void evaluate(class Context *ctx);

    std::string name;
    class Expression *expr;
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
    virtual void evaluate(class Context *ctx);

    class Expression *expr;
};

class FuncDefStatement : public Statement {
  public:
    FuncDefStatement(std::string _name);
    virtual ~FuncDefStatement();
    virtual void evaluate(class Context *ctx);

    std::string name;
};

} // namespace ast
} // namespace typhon

#endif