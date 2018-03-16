#ifndef SRC_DRIVER_H_
#define SRC_DRIVER_H_

#include <string>
#include <vector>

#include "ast.hh"
#include "context.hh"

namespace typhon {

class Driver {
  public:
    Driver(class Context &ctx);
    bool trace_scanning;
    bool trace_parsing;
    std::string streamname;
    void expr(ast::Expression *expr);
    void stmt(ast::Statement *stmt);

    bool parse_stream(std::istream &in, const std::string &sname = "stream input");
    bool parse_string(const std::string &input, const std::string &sname = "string stream");
    bool parse_file(const std::string &filename);
    // void error(const class location &l, const std::string &m);
    void error(const std::string &m);

    class Scanner *lexer;
    class Context &ctx;
};

} // namespace typhon

#endif
