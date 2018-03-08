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
    class typhon::ast::Expression* exprval;
}

%token<int> T_INTEGER
%token<sval> T_IDENT
%token T_NEWLINE
%token T_EOF 0

%token T_INDENT T_DEDENT

// keywords
%token T_DEF T_LET

// symbols
%token T_EQUALS T_COLON T_LPAREN T_RPAREN

// type
%type<exprval> expr
%type<stmtval> stmt simple_stmt assign_stmt reassign_stmt funcdef_stmt

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
expr: literal { $$ = new typhon::ast::Expression(); }
;

assign_stmt: T_LET T_IDENT T_EQUALS expr { $$ = new typhon::ast::AssignStatement(); }
;
reassign_stmt: T_IDENT T_EQUALS expr { $$ = new typhon::ast::ReassignStatement(); }
;
funcdef_stmt: T_DEF T_IDENT T_COLON suite { $$ = new typhon::ast::FuncDefStatement(*$2); }
;
simple_stmt: assign_stmt { $$ = $1; }
    | reassign_stmt { $$ = $1; }
;
stmt: simple_stmt { $$ = $1; }
    | funcdef_stmt { $$ = $1; }
;
stmts: stmts_
;
stmts_: /* empty */ | stmt stmts_ T_NEWLINE
;

suite: simple_stmt | T_NEWLINE T_INDENT stmts T_DEDENT
;
start: /* empty */
    | expr T_EOF { (new typhon::ast::ExpressionStatement($1))->evaluate(driver.ctx); }
    | stmt T_EOF { $1->evaluate(driver.ctx); }

%%

void typhon::Parser::error(const Parser::location_type& l, const std::string& m) {
    driver.error(l, m);
}
