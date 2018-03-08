#include <fstream>
#include <iostream>
#include <sstream>

#include "ast.hh"
#include "driver.hh"
#include "scanner.hh"

namespace typhon {

Driver::Driver(class Context &_ctx)
    : trace_scanning(false), trace_parsing(false), ctx(_ctx) {}

void Driver::show(ast::Expression *expr) {
    ast::TypedExpression *value = expr->evaluate(&ctx);
    std::cout << "val : " << value->to_string() << std::endl;
}

bool Driver::parse_stream(std::istream &in, const std::string &sname) {
    streamname = sname;

    Scanner scanner(&in);
    scanner.set_debug(trace_scanning);
    this->lexer = &scanner;

    Parser parser(*this);
    parser.set_debug_level(trace_parsing);
    return (parser.parse() == 0);
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

void Driver::error(const class location &l, const std::string &m) {
    std::cerr << l << ": " << m << std::endl;
}

void Driver::error(const std::string &m) { std::cerr << m << std::endl; }

} // namespace typhon
