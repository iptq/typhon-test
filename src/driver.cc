#include <fstream>
#include <iostream>
#include <sstream>

#include "ast.hh"
#include "driver.hh"
#include "parser.hh"
#include "scanner.hh"
#include "types.hh"

namespace typhon {

Driver::Driver(class Context &_ctx) : trace_scanning(false), trace_parsing(true), ctx(_ctx) {}

void Driver::expr(ast::Expression *expr) {
    ast::TypedExpression *typed_expr = expr->typecheck(&ctx);
    ast::TypedExpression *value = typed_expr->evaluate(&ctx);
    type::Type *type = value->type(&ctx);
    std::cout << type->to_string() << " : " << value->to_string() << std::endl;
}

void Driver::stmt(ast::Statement *stmt) {
    ast::ExpressionStatement *expr_stmt;
    if ((expr_stmt = dynamic_cast<ast::ExpressionStatement *>(stmt)))
        expr(expr_stmt->expr);
    stmt->evaluate(&ctx);
}

void Driver::block(ast::Block *block) {
    // TODO
    if (block->size() == 1)
        stmt(block->statements[0]);
    std::cout << "received " << block->statements.size() << " statement(s)" << std::endl;
}

bool Driver::parse_stream(std::istream &in, const std::string &sname) {
    streamname = sname;

    Scanner *scanner = new Scanner(&in);
    scanner->set_debug(trace_scanning);
    this->lexer = scanner;

    scanner->driver = this; // ref to parent
    scanner->state = typhonpstate_new();
    int status, token;
    do {
        token = lexer->lex(&scanner->semval, &scanner->locval);
        status = typhonpush_parse(scanner->state, token, &scanner->semval, &scanner->locval, this);
    } while (status == YYPUSH_MORE);
    typhonpstate_delete(scanner->state);
    return true;
}

bool Driver::parse_file(const std::string &filename) {
    std::ifstream in(filename.c_str());
    if (!in.good())
        return false;
    return parse_stream(in, filename);
}

bool Driver::parse_string(const std::string &input, const std::string &sname) {
    std::istringstream iss(input);
    return parse_stream(iss, sname);
}

// void Driver::error(const class location &l, const std::string &m) { std::cerr << l << ": " << m << std::endl; }

void Driver::error(const std::string &m) { std::cerr << m << std::endl; }

} // namespace typhon
