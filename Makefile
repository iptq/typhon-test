CC := clang++
LEX := flex++
YACC := bison -y

SRCDIR := src
BINDIR := bin
LIBDIR := lib
BUILDDIR := build

TC := $(BINDIR)/tc
TCI := $(BINDIR)/tci
TCLIB := $(BINDIR)/libtyphon.a

SRCEXT := cc
SOURCES := $(shell find $(SRCDIR) -type f -name '*.$(SRCEXT)' ! -name 'main.cc')
OBJECTS := $(patsubst $(SRCDIR)/%,$(BUILDDIR)/src/%,$(SOURCES:.$(SRCEXT)=.o))

LIBSOURCES := $(shell find $(LIBDIR) -type f -name '*.$(SRCEXT)')
LIBOBJECTS := $(patsubst $(LIBDIR)/%,$(BUILDDIR)/lib/%,$(LIBSOURCES:.$(SRCEXT)=.o))

INCLUDES := -I/usr/include `llvm-config --cxxflags` -Wno-unknown-warning-option
CFLAGS := $(INCLUDES) -fexceptions -O0 -std=c++14 -static -g -Wall
LDFLAGS := -L/usr/lib -lboost_program_options `llvm-config --system-libs --libs --ldflags core native`

all: $(TC) $(TCI) $(TCLIB)

$(TC): $(BUILDDIR)/src/parser.o $(BUILDDIR)/src/scanner.o $(OBJECTS) $(BUILDDIR)/src/compiler.o
	@mkdir -p $(BINDIR)
	$(CC) $(LDFLAGS) $^ -o $@ $(LIB)

$(TCI): $(BUILDDIR)/src/parser.o $(BUILDDIR)/src/scanner.o $(OBJECTS) $(BUILDDIR)/src/interpreter.o
	@mkdir -p $(BINDIR)
	$(CC) $(LDFLAGS) $^ -o $@ $(LIB)

$(BUILDDIR)/src/interpreter.o: $(SRCDIR)/main.cc
	@mkdir -p $(BUILDDIR)/src
	$(CC) $(CFLAGS) $(INC) -DINTERPRETER -c -o $@ $<

$(BUILDDIR)/src/compiler.o: $(SRCDIR)/main.cc
	@mkdir -p $(BUILDDIR)/src
	$(CC) $(CFLAGS) $(INC) -DCOMPILER -c -o $@ $<

$(BUILDDIR)/src/%.o: $(SRCDIR)/%.$(SRCEXT)
	@mkdir -p $(BUILDDIR)/src
	$(CC) $(CFLAGS) $(INC) -c -o $@ $<

# lib

$(TCLIB): $(LIBOBJECTS)
	ar rcs $@ $<

$(BUILDDIR)/lib/%.o: $(LIBDIR)/%.$(SRCEXT)
	@mkdir -p $(BUILDDIR)/lib
	$(CC) $(CFLAGS) $(INC) -c -o $@ $<

# pgen

$(SRCDIR)/scanner.cc: $(SRCDIR)/scanner.ll
	(cd $(SRCDIR); $(LEX) -o scanner.cc scanner.ll)

$(BUILDDIR)/src/scanner.o: $(SRCDIR)/scanner.cc
	@mkdir -p $(BUILDDIR)/src
	$(CC) $(CFLAGS) $(INC) -c -o $@ $<

$(SRCDIR)/parser.cc: $(SRCDIR)/parser.yy
	(cd $(SRCDIR); $(YACC) -t -o parser.cc parser.yy)

$(BUILDDIR)/src/parser.o: $(SRCDIR)/parser.cc
	@mkdir -p $(BUILDDIR)/src
	$(CC) $(CFLAGS) $(INC) -c -o $@ $<

clean:
	rm -rf $(BINDIR) $(BUILDDIR)
	rm -rf \
		$(SRCDIR)/location.hh $(SRCDIR)/position.hh $(SRCDIR)/stack.hh $(SRCDIR)/FlexLexer.h \
		$(SRCDIR)/parser.cc $(SRCDIR)/parser.hh \
		$(SRCDIR)/scanner.cc

.PHONY: clean
