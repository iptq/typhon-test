Grammar = Rule

Newline = Newline_
Newline_ = Newline_ + NEWLINE, EMPTY

Rule = Newline + Rule_
Rule_ = LHS + ":" + RHS + Newline + Rule_, EMPTY

LHS = IDENT
RHS = IDENT, STRING, \
    "[" + RHS + "]", \
    "{" + RHS + "}", \
    "(" + RHS + ")", \
    RHS + "|" + RHS, \
    RHS + "," + RHS
