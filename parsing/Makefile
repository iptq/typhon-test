CC = gcc
CFLAGS = -g -std=c11
LEX = flex
YACC = bison

.PHONY: all clean

all: parser

y.tab.c: parser.y
	$(YACC) -o $@ -d $^

y.tab.o: y.tab.c
	$(CC) $(CFLAGS) -c -o $@ $^

y.tab.h: y.tab.c

lex.yy.c: lexer.l
	$(LEX) -o $@ $^

lex.yy.o: lex.yy.c y.tab.h
	$(CC) $(CFLAGS) -c -o $@ $<

parser: y.tab.o lex.yy.o
	$(CC) $(CFLAGS) -o $@ $^

clean:
	rm -f *.o lex.yy.c y.tab.c y.tab.h parser