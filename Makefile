CC := clang++
LEX := flex++
YACC := bison -y

SRCDIR := src
BINDIR := bin
BUILDDIR := build

TC := $(BINDIR)/tc
TCI := $(BINDIR)/tci

SRCEXT := cc
SOURCES := $(shell find $(SRCDIR) -type f -name '*.$(SRCEXT)' ! -name 'main.cc')
OBJECTS := $(patsubst $(SRCDIR)/%,$(BUILDDIR)/%,$(SOURCES:.$(SRCEXT)=.o))
CFLAGS := -std=c++14 -static -g -Wall

all: $(TC) $(TCI)

$(TC): $(BUILDDIR)/parser.o $(BUILDDIR)/scanner.o $(OBJECTS) $(BUILDDIR)/compiler.o
	@mkdir -p $(BINDIR)
	$(CC) $^ -o $@ $(LIB)

$(TCI): $(BUILDDIR)/parser.o $(BUILDDIR)/scanner.o $(OBJECTS) $(BUILDDIR)/interpreter.o
	@mkdir -p $(BINDIR)
	$(CC) $^ -o $@ $(LIB)

$(BUILDDIR)/interpreter.o: $(SRCDIR)/main.cc
	@mkdir -p $(BUILDDIR)
	$(CC) $(CFLAGS) $(INC) -DINTERPRETER -c -o $@ $<

$(BUILDDIR)/compiler.o: $(SRCDIR)/main.cc
	@mkdir -p $(BUILDDIR)
	$(CC) $(CFLAGS) $(INC) -DCOMPILER -c -o $@ $<

$(BUILDDIR)/%.o: $(SRCDIR)/%.$(SRCEXT)
	@mkdir -p $(BUILDDIR)
	$(CC) $(CFLAGS) $(INC) -c -o $@ $<

# pgen

$(SRCDIR)/scanner.cc: $(SRCDIR)/scanner.ll
	(cd $(SRCDIR); $(LEX) -o scanner.cc scanner.ll)

$(BUILDDIR)/scanner.o: $(SRCDIR)/scanner.cc
	@mkdir -p $(BUILDDIR)
	$(CC) $(CFLAGS) $(INC) -c -o $@ $<

$(SRCDIR)/parser.cc: $(SRCDIR)/parser.yy
	(cd $(SRCDIR); $(YACC) -o parser.cc parser.yy)

$(BUILDDIR)/parser.o: $(SRCDIR)/parser.cc
	@mkdir -p $(BUILDDIR)
	$(CC) $(CFLAGS) $(INC) -c -o $@ $<

clean:
	rm -rf $(BINDIR) $(BUILDDIR)
	rm -rf \
		$(SRCDIR)/location.hh $(SRCDIR)/position.hh $(SRCDIR)/stack.hh $(SRCDIR)/FlexLexer.h \
		$(SRCDIR)/parser.cc $(SRCDIR)/parser.hh \
		$(SRCDIR)/scanner.cc

.PHONY: clean
