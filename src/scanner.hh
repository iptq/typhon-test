// $Id$

#ifndef SRC_SCANNER_H_
#define SRC_SCANNER_H_

#ifndef YY_DECL
#define YY_DECL int typhon::Scanner::lex(YYSTYPE *yylval, YYLTYPE *yylloc)
#endif

#ifndef __FLEX_LEXER_H
#define yyFlexLexer TyphonFlexLexer
#include "FlexLexer.h"
#undef yyFlexLexer
#endif

#include <string>

#include "ast.hh"
#include "common.hh"
#include "parser.hh"

namespace typhon {

class Scanner : public TyphonFlexLexer {
  public:
    Scanner(std::istream *arg_yyin = 0, std::ostream *arg_yyout = 0);

    virtual ~Scanner();
    virtual int lex(YYSTYPE *yylval, YYLTYPE *yylloc);
    void process_indent(std::string line);
    unsigned int white_count(std::string line);
    void set_debug(bool b);

    unsigned int indents[MAX_DEPTH];
    int level;
    unsigned int first;
    bool nesting;

    Driver *driver;
    typhonpstate *state;
    YYSTYPE semval;
    YYLTYPE locval;
};

} // namespace typhon

#endif
