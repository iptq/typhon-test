%{
#include <stdio.h>
#include <stdlib.h>
int yylex();
void yyerror(const char *s);
%}

%start expr
%union {
    int nInt;
    char* string;
};
%token <nInt> INTEGER
%token <string> IDENT
%type <nInt> expr
%%

expr: INTEGER expr0 { $$ = $1; }

expr0: /* empty */
     | INTEGER expr0

%%
main() {
    return yyparse();
}
void yyerror(const char* s) {
    fprintf(stderr, "%s\n",s);
}
yywrap() {
    return 1;
}