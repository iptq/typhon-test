%{

#include <stdio.h>
#include <string>
#include <vector>

#include "ast.hh"

%}

%code requires {
    namespace typhon { class Driver; }
}

%debug
%defines
%output "parser.cc"
// %skeleton "lalr1.cc"
// %define "parser_class_name" { Parser }
%name-prefix "typhon"

%define api.pure full
%define api.push-pull push 

%locations
// %initial-action
// {
//     @$.begin.filename = @$.end.filename = &driver.streamname;
// };

%parse-param { typhon::Driver* driver }
%error-verbose

%union {
    int             ival;
    char            cval;
    double 			fval;
    std::string*	sval;

    typhon::ast::BINOP binop;
    typhon::ast::Statement* stmtval;
    typhon::ast::Block* block;
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
%type<exprval> expr literal variable funcapp
%type<stmtval> stmt expr_stmt simple_stmt assign_stmt reassign_stmt funcdef_stmt
%type<block> stmts

%start start

%{

#include "driver.hh"
#include "scanner.hh"

#undef yylex
#define yylex driver->lexer->lex

int typhonerror(YYLTYPE *location, typhon::Driver* driver, std::string line);

%}

%%

literal: T_INTEGER { $$ = new typhon::ast::IntegerLiteralExpression($1); }
    | T_CHAR { $$ = new typhon::ast::CharacterLiteralExpression($1); }
;
variable: T_IDENT { $$ = new typhon::ast::VariableExpression(*$1); }
;
funcapp: T_IDENT T_LPAREN T_RPAREN { $$ = new typhon::ast::IntegerLiteralExpression(1); }
;
expr: literal { $$ = $1; }
    | variable { $$ = $1; }
    | funcapp { $$ = $1; }
    | expr T_BINOP expr { $$ = new typhon::ast::BinaryOperationExpression($1, $2, $3); }
;

assign_stmt: T_LET T_IDENT T_EQUALS expr { $$ = new typhon::ast::AssignStatement(*$2, $4); }
;
reassign_stmt: T_IDENT T_EQUALS expr { $$ = new typhon::ast::ReassignStatement(); }
;
expr_stmt: expr { $$ = new typhon::ast::ExpressionStatement($1); }
;
funcdef_stmt: T_DEF T_IDENT T_LPAREN T_RPAREN T_COLON suite { $$ = new typhon::ast::FuncDefStatement(*$2); }
;
simple_stmt: assign_stmt { $$ = $1; }
    | reassign_stmt { $$ = $1; }
    | expr_stmt { $$ = $1; }
;
stmt: simple_stmt { $$ = $1; }
    | funcdef_stmt { $$ = $1; }
;

stmts: /* empty */ { $$ = new typhon::ast::Block(); }
    | stmts stmt newlines { $1->statements.push_back($2); $$ = $1; }
;
newlines: /* empty */ | T_NEWLINE newlines ;

suite: simple_stmt | newlines T_INDENT stmts T_DEDENT ;
start: stmts { driver->handle_block($1); }

%%

int typhonerror(YYLTYPE *location, typhon::Driver* driver, std::string line) {
    std::cerr << "Error: " << line << std::endl;
    return 0;
}