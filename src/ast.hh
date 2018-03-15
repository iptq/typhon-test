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
    virtual TypedExpression *typecheck(Context *ctx) = 0;
    virtual std::string to_string() { return "unevaluated expr"; }
};

class TypedExpression : public Expression {
  public:
    virtual TypedExpression *typecheck(Context *ctx) { return this; }
    virtual TypedExpression *evaluate(Context *ctx);
    virtual type::Type *type(Context *ctx) = 0;
};

class LiteralExpression : public TypedExpression {};

class IntegerLiteralExpression : public LiteralExpression {
  public:
    IntegerLiteralExpression(int _n);
    type::Type *type(Context *ctx);
    std::string to_string() { return std::to_string(n); }

    int n;
};

class CharacterLiteralExpression : public LiteralExpression {
  public:
    CharacterLiteralExpression(char _c);
    type::Type *type(Context *ctx);
    std::string to_string() { return "'" + std::to_string(c) + "'"; }

    char c;
};

class VariableExpression : public TypedExpression {
  public:
    VariableExpression(std::string _name);
    TypedExpression *evaluate(Context *ctx);
    std::string name;
    type::Type *type(Context *ctx);
};

class BinaryOperationExpression : public Expression {
  public:
    BinaryOperationExpression(Expression *_left, enum BINOP _op, Expression *_right);
    virtual TypedExpression *typecheck(Context *ctx);

    Expression *left;
    enum BINOP op;
    Expression *right;
};

class TypedBinaryOperationExpression : public BinaryOperationExpression, public TypedExpression {
  public:
    TypedBinaryOperationExpression(type::Type *type, TypedExpression *_left, enum BINOP _op, TypedExpression *_right);
    TypedExpression *evaluate(Context *ctx);
    type::Type *type(Context *ctx);

    TypedExpression *left;
    enum BINOP op;
    TypedExpression *right;
    type::Type *_type;
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
    Expression *expr;
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

    Expression *expr;
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