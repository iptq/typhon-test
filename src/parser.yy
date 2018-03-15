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
    int             ival;
    char            cval;
    double 			fval;
    std::string*	sval;

    typhon::ast::BINOP binop;
    typhon::ast::Statement* stmtval;
    typhon::ast::Expression* exprval;
}

%token<ival> T_INTEGER
%token<cval> T_CHAR
%token<sval> T_IDENT T_STRING
%token T_NEWLINE
%token T_EOF 0

%token T_INDENT T_DEDENT

// keywords
%token T_DEF T_LET

// symbols
%token T_EQUALS T_COLON T_LPAREN T_RPAREN
%token<binop> T_BINOP

// type
%type<exprval> expr literal variable
%type<stmtval> stmt simple_stmt assign_stmt reassign_stmt funcdef_stmt

%start start

%{

#include "driver.hh"
#include "scanner.hh"

#undef yylex
#define yylex driver.lexer->lex

%}

%%

literal: T_INTEGER { $$ = new typhon::ast::IntegerLiteralExpression($1); }
    | T_CHAR { $$ = new typhon::ast::CharacterLiteralExpression($1); }
;
variable: T_IDENT { $$ = new typhon::ast::VariableExpression(*$1); }
;
expr: literal { $$ = $1; }
    | variable { $$ = $1; }
    | expr T_BINOP expr { $$ = new typhon::ast::BinaryOperationExpression($1, $2, $3); }
;

assign_stmt: T_LET T_IDENT T_EQUALS expr { $$ = new typhon::ast::AssignStatement(*$2, $4); }
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
    | expr T_EOF { driver.show($1->typecheck(&driver.ctx)->evaluate(&driver.ctx)); }
    | stmt T_EOF { $1->evaluate(&driver.ctx); }

%%

void typhon::Parser::error(const Parser::location_type& l, const std::string& m) {
    driver.error(l, m);
}
