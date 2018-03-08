CC := clang++
LEX := flex++
YACC := bison -y

SRCDIR := src
BINDIR := bin
BUILDDIR := build
TARGET := $(BINDIR)/tci

SRCEXT := cc
SOURCES := $(shell find $(SRCDIR) -type f -name *.$(SRCEXT))
OBJECTS := $(patsubst $(SRCDIR)/%,$(BUILDDIR)/%,$(SOURCES:.$(SRCEXT)=.o))
CFLAGS := -std=c++14 -static -g -Wall

all: $(TARGET)

$(TARGET): $(BUILDDIR)/parser.o $(BUILDDIR)/scanner.o $(OBJECTS)
	@mkdir -p $(BINDIR)
	$(CC) $^ -o $(TARGET) $(LIB)

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
