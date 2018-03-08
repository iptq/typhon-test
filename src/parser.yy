%{

#include <stdio.h>
#include <string>
#include <vector>

#include "ast.hh"

%}

%debug
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

%token<int> T_INTEGER
%token<string> T_IDENT
%token T_NEWLINE
%token T_EOF 0

// symbols
%token T_EQUALS

%start start

%{

#include "driver.hh"
#include "scanner.hh"

#undef yylex
#define yylex driver.lexer->lex

%}

%%

literal: T_INTEGER
;
expr: literal
;
assign_stmt: T_IDENT T_EQUALS expr
;
stmt: assign_stmt
;
start: /* empty */ | stmt T_EOF

%%

void typhon::Parser::error(const Parser::location_type& l, const std::string& m) {
    driver.error(l, m);
}
