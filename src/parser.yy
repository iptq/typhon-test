%{

#include <stdio.h>
#include <string>
#include <vector>

#include "expression.h"

%}

%debug
%start start
%defines
%skeleton "lalr1.cc"
%name-prefix "typhon"
%define "parser_class_name" { Parser }

%locations
%initial-action
{
    @$.begin.filename = @$.end.filename = &driver.streamname;
};

%parse-param { class Driver& driver }
%error-verbose

%union {
    int  			ival;
    double 			fval;
    std::string*	sval;
}

%token T_INTEGER
%token T_NEWLINE T_EOF

%{

#include "driver.hh"
#include "scanner.hh"

#undef yylex
#define yylex driver.lexer->lex

%}

%%

statement: T_INTEGER

;

start: /* empty */
    | start ';'
    | start statement T_EOF

%%

void typhon::Parser::error(const Parser::location_type& l, const std::string& m) {
    driver.error(l, m);
}
