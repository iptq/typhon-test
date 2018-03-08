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
CFLAGS := -std=c++14 -static -g -Wall -Werror

all: $(TARGET)

$(TARGET): $(SRCDIR)/scanner.cc $(SRCDIR)/parser.cc $(OBJECTS)
	@mkdir -p $(BINDIR)
	$(CC) $^ -o $(TARGET) $(LIB)

$(SRCDIR)/scanner.cc: $(SRCDIR)/scanner.ll
	(cd $(SRCDIR); $(LEX) -o scanner.cc scanner.ll)

$(SRCDIR)/parser.cc: $(SRCDIR)/parser.yy
	(cd $(SRCDIR); $(YACC) -o parser.cc parser.yy)

$(BUILDDIR)/%.o: $(SRCDIR)/%.$(SRCEXT)
	@mkdir -p $(BUILDDIR)
	$(CC) $(CFLAGS) $(INC) -c -o $@ $<

clean:
	rm -rf $(BINDIR) $(BUILDDIR)
	rm -rf \
		$(SRCDIR)/location.hh $(SRCDIR)/position.hh $(SRCDIR)/stack.hh $(SRCDIR)/FlexLexer.h \
		$(SRCDIR)/parser.cc $(SRCDIR)/parser.hh \
		$(SRCDIR)/scanner.cc

.PHONY: clean
