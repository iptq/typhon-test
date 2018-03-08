# $Id$

AM_CFLAGS = -W -Wall -Wextra -ansi
AM_CXXFLAGS = -W -Wall -Wextra -ansi

noinst_LIBRARIES = libtyphon.a

libtyphon_a_SOURCES = \
	parser.yy scanner.ll parser.h scanner.h y.tab.h \
	location.hh position.hh stack.hh FlexLexer.h \
	driver.cc driver.h expression.h

bin_PROGRAMS = ../tci

exprtest_SOURCES = exprtest.cc
exprtest_DEPENDENCIES = libtyphon.a

LIBS = libtyphon.a

# this output override is needed because the c++ scanner is outputted into
# lex.yy.cc and the automake ylwrap script only checks for lex.yy.c
AM_LFLAGS = -olex.yy.c

EXTRA_DIST = exprtest.txt \
	exprtest.vcproj libtyphon.vcproj \
	Makefile.plain

extraclean:
	rm -f parser.cc parser.h scanner.cc

rebuild: clean extraclean all
