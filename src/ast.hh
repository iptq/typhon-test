#ifndef SRC_AST_H_
#define SRC_AST_H_

#include <string>

#include "context.hh"
#include "exceptions.hh"
#include "types.hh"

namespace typhon {
namespace ast {

enum BINOP {
    O_PLUS,
    O_MINUS,
    O_STAR,
    O_SLASH,
};

class TypedExpression;

class Expression {
  public:
    virtual TypedExpression *evaluate(Context *ctx);
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
    TypedExpression *evaluate(Context *ctx);
    std::string to_string() { return std::to_string(n); }
    int n;
};

class VariableExpression : public TypedExpression {
  public:
    VariableExpression(std::string _name);
    TypedExpression *evaluate(Context *ctx);
    std::string name;
};

class BinaryOperationExpression : public TypedExpression {
  public:
    BinaryOperationExpression(Expression *_left, enum BINOP _op, Expression *_right);
    TypedExpression *evaluate(Context *ctx);

    Expression *left;
    enum BINOP op;
    Expression *right;
};

class Statement {
  public:
    virtual void evaluate(Context *ctx) {}
};

class AssignStatement : public Statement {
  public:
    AssignStatement(std::string _name, Expression *_expr);
    virtual ~AssignStatement();
    void evaluate(Context *ctx);

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
    ExpressionStatement(Expression *_expr);
    virtual ~ExpressionStatement();
    void evaluate(Context *ctx);

    class Expression *expr;
};

class FuncDefStatement : public Statement {
  public:
    FuncDefStatement(std::string _name);
    virtual ~FuncDefStatement();
    void evaluate(Context *ctx);

    std::string name;
};

} // namespace ast
} // namespace typhon

#endif