// $Id$

#ifndef SRC_SCANNER_H_
#define SRC_SCANNER_H_

#ifndef YY_DECL
#define YY_DECL                                                                \
    typhon::Parser::token_type typhon::Scanner::lex(                           \
        typhon::Parser::semantic_type *yylval,                                 \
        typhon::Parser::location_type *yylloc)
#endif

#ifndef __FLEX_LEXER_H
#define yyFlexLexer TyphonFlexLexer
#include "FlexLexer.h"
#undef yyFlexLexer
#endif

#include "parser.hh"

namespace typhon {

class Scanner : public TyphonFlexLexer {
  public:
    Scanner(std::istream *arg_yyin = 0, std::ostream *arg_yyout = 0);

    virtual ~Scanner();
    virtual Parser::token_type lex(Parser::semantic_type *yylval,
                                   Parser::location_type *yylloc);
    void set_debug(bool b);
};

} // namespace typhon

#endif
