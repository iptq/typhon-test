%{
#include "y.tab.h"
%}

%option noyywrap

%%

[0-9]+ { yylval.nInt = atoi(yytext); return INTEGER; }
[A-Za-z_][A-Za-z0-9_]* { yylval.string = yytext; return IDENT; }
[\ \t\n]+ { } // ignore newlines
. { fprintf(stderr, "Unrecognized token\n"); exit(1); }

%%