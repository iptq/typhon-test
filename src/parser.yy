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
    class typhon::ast::Statement* stmtval;
}

%token<int> T_INTEGER
%token<sval> T_IDENT
%token T_NEWLINE
%token T_EOF 0

%token T_INDENT T_DEDENT

// keywords
%token T_DEF

// symbols
%token T_EQUALS T_COLON T_LPAREN T_RPAREN

// type
%type<stmtval> stmt  funcdef_stmt

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
funcdef_stmt: T_DEF T_IDENT T_COLON suite { $$ = new typhon::ast::FuncDef(*$2); }
;
simple_stmt: assign_stmt
;
stmt: simple_stmt { $$ = new typhon::ast::Statement(); }
    | funcdef_stmt { $$ = $1; }
;
stmts: stmts_
;
stmts_: /* empty */ | stmt stmts_ T_NEWLINE
;

suite: simple_stmt | T_NEWLINE T_INDENT stmts T_DEDENT
;
start: /* empty */
    | stmt T_EOF { $1->evaluate(driver.ctx); }

%%

void typhon::Parser::error(const Parser::location_type& l, const std::string& m) {
    driver.error(l, m);
}
