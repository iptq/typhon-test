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
    // initialize the initial location object
    @$.begin.filename = @$.end.filename = &driver.streamname;
};

%parse-param { class Driver& driver }
%error-verbose

%union {
    int  			integerVal;
    double 			doubleVal;
    std::string*		stringVal;
    class CalcNode*		calcnode;
}

%token			END	     0	"end of file"
%token			EOL		"end of line"
%token <integerVal> 	INTEGER		"integer"
%token <doubleVal> 	DOUBLE		"double"
%token <stringVal> 	STRING		"string"

%type <calcnode>	constant variable
%type <calcnode>	atomexpr powexpr unaryexpr mulexpr addexpr expr

%destructor { delete $$; } STRING
%destructor { delete $$; } constant variable
%destructor { delete $$; } atomexpr powexpr unaryexpr mulexpr addexpr expr

%{

#include "driver.hh"
#include "scanner.hh"

#undef yylex
#define yylex driver.lexer->lex

%}

%%

constant : INTEGER
           {
	       $$ = new CNConstant($1);
	   }
         | DOUBLE
           {
	       $$ = new CNConstant($1);
	   }

variable : STRING
           {
	       if (!driver.calc.existsVariable(*$1)) {
		   delete $1;
		   YYERROR;
	       }
	       else {
		   $$ = new CNConstant( driver.calc.getVariable(*$1) );
		   delete $1;
	       }
	   }

atomexpr : constant
           {
	       $$ = $1;
	   }
         | variable
           {
	       $$ = $1;
	   }
         | '(' expr ')'
           {
	       $$ = $2;
	   }

powexpr	: atomexpr
          {
	      $$ = $1;
	  }
        | atomexpr '^' powexpr
          {
	      $$ = new CNPower($1, $3);
	  }

unaryexpr : powexpr
            {
		$$ = $1;
	    }
          | '+' powexpr
            {
		$$ = $2;
	    }
          | '-' powexpr
            {
		$$ = new CNNegate($2);
	    }

mulexpr : unaryexpr
          {
	      $$ = $1;
	  }
        | mulexpr '*' unaryexpr
          {
	      $$ = new CNMultiply($1, $3);
	  }
        | mulexpr '/' unaryexpr
          {
	      $$ = new CNDivide($1, $3);
	  }
        | mulexpr '%' unaryexpr
          {
	      $$ = new CNModulo($1, $3);
	  }

addexpr : mulexpr
          {
	      $$ = $1;
	  }
        | addexpr '+' mulexpr
          {
	      $$ = new CNAdd($1, $3);
	  }
        | addexpr '-' mulexpr
          {
	      $$ = new CNSubtract($1, $3);
	  }

expr	: addexpr
          {
	      $$ = $1;
	  }

assignment : STRING '=' expr
             {
		 driver.calc.variables[*$1] = $3->evaluate();
		 std::cout << "Setting variable " << *$1
			   << " = " << driver.calc.variables[*$1] << "\n";
		 delete $1;
		 delete $3;
	     }

start	: /* empty */
        | start ';'
        | start EOL
	| start assignment ';'
	| start assignment EOL
	| start assignment END
        | start expr ';'
          {
	      driver.calc.expressions.push_back($2);
	  }
        | start expr EOL
          {
	      driver.calc.expressions.push_back($2);
	  }
        | start expr END
          {
	      driver.calc.expressions.push_back($2);
	  }

%%

void typhon::Parser::error(const Parser::location_type& l,
			    const std::string& m)
{
    driver.error(l, m);
}
