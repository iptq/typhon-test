# $Id$

AM_CFLAGS = -W -Wall -Wextra -ansi
AM_CXXFLAGS = -W -Wall -Wextra -ansi

noinst_LIBRARIES = libtyphon.a

libtyphon_a_SOURCES = \
	parser.yy scanner.ll parser.h scanner.hh y.tab.h \
	location.hh position.hh stack.hh FlexLexer.h \
	driver.cc driver.hh expression.h

bin_PROGRAMS = tci

tci_SOURCES = exprtest.cc
tci_DEPENDENCIES = libtyphon.a

LIBS = libtyphon.a

# this output override is needed because the c++ scanner is outputted into
# lex.yy.cc and the automake ylwrap script only checks for lex.yy.c
AM_LFLAGS = -olex.yy.c

extraclean:
	rm -f parser.cc parser.hh scanner.cc

rebuild: clean extraclean all
