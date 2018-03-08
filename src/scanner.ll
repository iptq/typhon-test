%{

#include <string>

#include "scanner.hh"

typedef typhon::Parser::token token;
typedef typhon::Parser::token_type token_type;

#define yyterminate() return token::T_EOF
#define YY_NO_UNISTD_H

%}

%option c++
%option prefix="Typhon"
%option batch
%option debug
%option yywrap nounput
%option stack

%{
#define YY_USER_ACTION  yylloc->columns(yyleng);
%}

%%

%{
    yylloc->step();
%}


[0-9]+ {
    yylval->ival = atoi(yytext);
    return token::T_INTEGER;
}

%%

namespace typhon {

Scanner::Scanner(std::istream* in, std::ostream* out) : TyphonFlexLexer(in, out) {
}

Scanner::~Scanner() {
}

void Scanner::set_debug(bool b) {
    yy_flex_debug = b;
}

}

#ifdef yylex
#undef yylex
#endif

int TyphonFlexLexer::yylex() {
    std::cerr << "in TyphonFlexLexer::yylex() !" << std::endl;
    return 0;
}

int TyphonFlexLexer::yywrap() {
    return 1;
}