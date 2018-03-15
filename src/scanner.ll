%{

#include <deque>
#include <string>

#include "scanner.hh"

// typedef typhon::Scanner::token token;
// typedef typhon::Scanner::token_type token_type;

#define yyterminate() process_indent(""); return T_EOF
#define YY_NO_UNISTD_H

%}

%option c++
%option prefix="Typhon"
%option batch
%option debug
%option noyywrap unput
%option stack

%{
#define YY_USER_ACTION  // yylloc->columns(yyleng);
%}

%%

%{
    // yylloc->step();
%}

^[ ]*\n { /* ignore blank lines */ }
^[ ]*[^ \n]+ {
    int last = yyleng - 1;
    process_indent(std::string(yytext));
    while ((last >= 0) && (yytext[last] != ' '))
        unput(yytext[last--]);
}

\r | \n {}

\= { return T_EQUALS; }
\: { return T_COLON; }
\( { return T_LPAREN; }
\) { return T_RPAREN; }

\+ { yylval->binop = ast::O_PLUS; return T_BINOP; }

def { return T_DEF; }
let { return T_LET; }

[0-9]+ {
    yylval->ival = atoi(yytext);
    return T_INTEGER;
}

\'(\\t|\\r|\\n|\\\'|\\\"|\\\\|[^\\])*\' {
    yylval->cval = yytext[1];
    return T_CHAR;
}

\"(\\t|\\r|\\n|\\\'|\\\"|\\\\|[^\\])*\" {
    yylval->sval = new std::string(yytext);
    return T_STRING;
}

[a-zA-Z_][a-zA-Z0-9_]* {
    yylval->sval = new std::string(yytext);
    return T_IDENT;
}

%%

namespace typhon {

Scanner::Scanner(std::istream* in, std::ostream* out) : TyphonFlexLexer(in, out), level(0), first(1), nesting(false) {
    indents[level] = 0;
}

Scanner::~Scanner() {
}

unsigned int Scanner::white_count(std::string line) {
    unsigned int count = 0;
    for (auto it = line.begin(); it != line.end() and *it == ' '; ++it)
        ++count;
    return count;
}

void Scanner::process_indent(std::string line) {
    if (nesting)
        return;
    
    unsigned int indent = white_count(line);
    if (indent == indents[level]) {
        
    }
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
