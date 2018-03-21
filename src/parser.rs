// auto-generated: "lalrpop 0.14.0"
use ast::{Expr, Program, Stmt};
use lexer::{LexError, Token};
#[allow(unused_extern_crates)]
extern crate lalrpop_util as __lalrpop_util;

mod __parse__Line {
    #![allow(non_snake_case, non_camel_case_types, unused_mut, unused_variables, unused_imports, unused_parens)]

    use ast::{Expr, Program, Stmt};
    use lexer::{LexError, Token};
    #[allow(unused_extern_crates)]
    extern crate lalrpop_util as __lalrpop_util;
    use super::__ToTriple;
    #[allow(dead_code)]
    pub enum __Symbol<'input>
     {
        Term_22_28_22(Token<'input>),
        Term_22_29_22(Token<'input>),
        Term_22Colon_22(&'input str),
        Term_22EOF_22(Token<'input>),
        Term_22Newline_22(Token<'input>),
        Nt_22EOF_22_3f(::std::option::Option<Token<'input>>),
        Nt_28_3cStmt_3e_20_22Newline_22_29(Stmt),
        Nt_28_3cStmt_3e_20_22Newline_22_29_2a(::std::vec::Vec<Stmt>),
        Nt_28_3cStmt_3e_20_22Newline_22_29_2b(::std::vec::Vec<Stmt>),
        NtLine(Stmt),
        NtProgram(Program),
        NtStmt(Stmt),
        NtStmt_3f(::std::option::Option<Stmt>),
        NtStmts(Vec<Stmt>),
        Nt____Line(Stmt),
        Nt____Program(Program),
    }
    const __ACTION: &'static [i32] = &[
        // State 0
        0, 0, 4, 0, 0,
        // State 1
        0, 0, 0, 0, 0,
        // State 2
        0, 0, 0, 5, 0,
        // State 3
        0, 0, 0, -12, 0,
        // State 4
        0, 0, 0, 0, 0,
    ];
    const __EOF_ACTION: &'static [i32] = &[
        // State 0
        0,
        // State 1
        -19,
        // State 2
        -9,
        // State 3
        -12,
        // State 4
        -8,
    ];
    const __GOTO: &'static [i32] = &[
        // State 0
        0, 0, 0, 0, 2, 0, 3, 0, 0, 0, 0,
        // State 1
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        // State 2
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        // State 3
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        // State 4
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    ];
    fn __expected_tokens(__state: usize) -> Vec<::std::string::String> {
        const __TERMINAL: &'static [&'static str] = &[
            r###""(""###,
            r###"")""###,
            r###""Colon""###,
            r###""EOF""###,
            r###""Newline""###,
        ];
        __ACTION[(__state * 5)..].iter().zip(__TERMINAL).filter_map(|(&state, terminal)| {
            if state == 0 {
                None
            } else {
                Some(terminal.to_string())
            }
        }).collect()
    }
    #[allow(dead_code)]
    pub fn parse_Line<
        'input,
        __TOKEN: __ToTriple<'input, Error=LexError>,
        __TOKENS: IntoIterator<Item=__TOKEN>,
    >(
        __tokens0: __TOKENS,
    ) -> Result<Stmt, __lalrpop_util::ParseError<usize, Token<'input>, LexError>>
    {
        let __tokens = __tokens0.into_iter();
        let mut __tokens = __tokens.map(|t| __ToTriple::to_triple(t));
        let mut __states = vec![0_i32];
        let mut __symbols = vec![];
        let mut __integer;
        let mut __lookahead;
        let __last_location = &mut Default::default();
        '__shift: loop {
            __lookahead = match __tokens.next() {
                Some(Ok(v)) => v,
                None => break '__shift,
                Some(Err(e)) => return Err(__lalrpop_util::ParseError::User { error: e }),
            };
            *__last_location = __lookahead.2.clone();
            __integer = match __lookahead.1 {
                Token::LeftParen if true => 0,
                Token::RightParen if true => 1,
                Token::Symbol(_) if true => 2,
                Token::EOF if true => 3,
                Token::Newline if true => 4,
                _ => {
                    let __state = *__states.last().unwrap() as usize;
                    let __error = __lalrpop_util::ParseError::UnrecognizedToken {
                        token: Some(__lookahead),
                        expected: __expected_tokens(__state),
                    };
                    return Err(__error);
                }
            };
            '__inner: loop {
                let __state = *__states.last().unwrap() as usize;
                let __action = __ACTION[__state * 5 + __integer];
                if __action > 0 {
                    let __symbol = match __integer {
                        0 => match __lookahead.1 {
                            __tok @ Token::LeftParen => __Symbol::Term_22_28_22((__tok)),
                            _ => unreachable!(),
                        },
                        1 => match __lookahead.1 {
                            __tok @ Token::RightParen => __Symbol::Term_22_29_22((__tok)),
                            _ => unreachable!(),
                        },
                        2 => match __lookahead.1 {
                            Token::Symbol(__tok0) => __Symbol::Term_22Colon_22((__tok0)),
                            _ => unreachable!(),
                        },
                        3 => match __lookahead.1 {
                            __tok @ Token::EOF => __Symbol::Term_22EOF_22((__tok)),
                            _ => unreachable!(),
                        },
                        4 => match __lookahead.1 {
                            __tok @ Token::Newline => __Symbol::Term_22Newline_22((__tok)),
                            _ => unreachable!(),
                        },
                        _ => unreachable!(),
                    };
                    __states.push(__action - 1);
                    __symbols.push((__lookahead.0, __symbol, __lookahead.2));
                    continue '__shift;
                } else if __action < 0 {
                    if let Some(r) = __reduce(__action, Some(&__lookahead.0), &mut __states, &mut __symbols, ::std::marker::PhantomData::<()>) {
                        if r.is_err() {
                            return r;
                        }
                        return Err(__lalrpop_util::ParseError::ExtraToken { token: __lookahead });
                    }
                } else {
                    let mut __err_lookahead = Some(__lookahead);
                    let mut __err_integer: Option<usize> = Some(__integer);
                    let __state = *__states.last().unwrap() as usize;
                    let __error = __lalrpop_util::ParseError::UnrecognizedToken {
                        token: __err_lookahead,
                        expected: __expected_tokens(__state),
                    };
                    return Err(__error)
                }
            }
        }
        loop {
            let __state = *__states.last().unwrap() as usize;
            let __action = __EOF_ACTION[__state];
            if __action < 0 {
                if let Some(r) = __reduce(__action, None, &mut __states, &mut __symbols, ::std::marker::PhantomData::<()>) {
                    return r;
                }
            } else {
                let mut __err_lookahead = None;
                let mut __err_integer: Option<usize> = None;
                let __state = *__states.last().unwrap() as usize;
                let __error = __lalrpop_util::ParseError::UnrecognizedToken {
                    token: __err_lookahead,
                    expected: __expected_tokens(__state),
                };
                return Err(__error)
            }
        }
    }
    pub fn __reduce<
        'input,
    >(
        __action: i32,
        __lookahead_start: Option<&usize>,
        __states: &mut ::std::vec::Vec<i32>,
        __symbols: &mut ::std::vec::Vec<(usize,__Symbol<'input>,usize)>,
        _: ::std::marker::PhantomData<()>,
    ) -> Option<Result<Stmt,__lalrpop_util::ParseError<usize, Token<'input>, LexError>>>
    {
        let __nonterminal = match -__action {
            1 => {
                // "EOF"? = "EOF" => ActionFn(6);
                let __sym0 = __pop_Term_22EOF_22(__symbols);
                let __start = __sym0.0.clone();
                let __end = __sym0.2.clone();
                let __nt = super::__action6::<>(__sym0);
                let __states_len = __states.len();
                __states.truncate(__states_len - 1);
                __symbols.push((__start, __Symbol::Nt_22EOF_22_3f(__nt), __end));
                0
            }
            2 => {
                // "EOF"? =  => ActionFn(7);
                let __start = __symbols.last().map(|s| s.2.clone()).unwrap_or_default();
                let __end = __lookahead_start.cloned().unwrap_or_else(|| __start.clone());
                let __nt = super::__action7::<>(&__start, &__end);
                let __states_len = __states.len();
                __states.truncate(__states_len - 0);
                __symbols.push((__start, __Symbol::Nt_22EOF_22_3f(__nt), __end));
                0
            }
            3 => {
                // (<Stmt> "Newline") = Stmt, "Newline" => ActionFn(12);
                let __sym1 = __pop_Term_22Newline_22(__symbols);
                let __sym0 = __pop_NtStmt(__symbols);
                let __start = __sym0.0.clone();
                let __end = __sym1.2.clone();
                let __nt = super::__action12::<>(__sym0, __sym1);
                let __states_len = __states.len();
                __states.truncate(__states_len - 2);
                __symbols.push((__start, __Symbol::Nt_28_3cStmt_3e_20_22Newline_22_29(__nt), __end));
                1
            }
            4 => {
                // (<Stmt> "Newline")* =  => ActionFn(10);
                let __start = __symbols.last().map(|s| s.2.clone()).unwrap_or_default();
                let __end = __lookahead_start.cloned().unwrap_or_else(|| __start.clone());
                let __nt = super::__action10::<>(&__start, &__end);
                let __states_len = __states.len();
                __states.truncate(__states_len - 0);
                __symbols.push((__start, __Symbol::Nt_28_3cStmt_3e_20_22Newline_22_29_2a(__nt), __end));
                2
            }
            5 => {
                // (<Stmt> "Newline")* = (<Stmt> "Newline")+ => ActionFn(11);
                let __sym0 = __pop_Nt_28_3cStmt_3e_20_22Newline_22_29_2b(__symbols);
                let __start = __sym0.0.clone();
                let __end = __sym0.2.clone();
                let __nt = super::__action11::<>(__sym0);
                let __states_len = __states.len();
                __states.truncate(__states_len - 1);
                __symbols.push((__start, __Symbol::Nt_28_3cStmt_3e_20_22Newline_22_29_2a(__nt), __end));
                2
            }
            6 => {
                // (<Stmt> "Newline")+ = Stmt, "Newline" => ActionFn(19);
                let __sym1 = __pop_Term_22Newline_22(__symbols);
                let __sym0 = __pop_NtStmt(__symbols);
                let __start = __sym0.0.clone();
                let __end = __sym1.2.clone();
                let __nt = super::__action19::<>(__sym0, __sym1);
                let __states_len = __states.len();
                __states.truncate(__states_len - 2);
                __symbols.push((__start, __Symbol::Nt_28_3cStmt_3e_20_22Newline_22_29_2b(__nt), __end));
                3
            }
            7 => {
                // (<Stmt> "Newline")+ = (<Stmt> "Newline")+, Stmt, "Newline" => ActionFn(20);
                let __sym2 = __pop_Term_22Newline_22(__symbols);
                let __sym1 = __pop_NtStmt(__symbols);
                let __sym0 = __pop_Nt_28_3cStmt_3e_20_22Newline_22_29_2b(__symbols);
                let __start = __sym0.0.clone();
                let __end = __sym2.2.clone();
                let __nt = super::__action20::<>(__sym0, __sym1, __sym2);
                let __states_len = __states.len();
                __states.truncate(__states_len - 3);
                __symbols.push((__start, __Symbol::Nt_28_3cStmt_3e_20_22Newline_22_29_2b(__nt), __end));
                3
            }
            8 => {
                // Line = Stmt, "EOF" => ActionFn(15);
                let __sym1 = __pop_Term_22EOF_22(__symbols);
                let __sym0 = __pop_NtStmt(__symbols);
                let __start = __sym0.0.clone();
                let __end = __sym1.2.clone();
                let __nt = super::__action15::<>(__sym0, __sym1);
                let __states_len = __states.len();
                __states.truncate(__states_len - 2);
                __symbols.push((__start, __Symbol::NtLine(__nt), __end));
                4
            }
            9 => {
                // Line = Stmt => ActionFn(16);
                let __sym0 = __pop_NtStmt(__symbols);
                let __start = __sym0.0.clone();
                let __end = __sym0.2.clone();
                let __nt = super::__action16::<>(__sym0);
                let __states_len = __states.len();
                __states.truncate(__states_len - 1);
                __symbols.push((__start, __Symbol::NtLine(__nt), __end));
                4
            }
            10 => {
                // Program = Stmts, "EOF" => ActionFn(17);
                let __sym1 = __pop_Term_22EOF_22(__symbols);
                let __sym0 = __pop_NtStmts(__symbols);
                let __start = __sym0.0.clone();
                let __end = __sym1.2.clone();
                let __nt = super::__action17::<>(__sym0, __sym1);
                let __states_len = __states.len();
                __states.truncate(__states_len - 2);
                __symbols.push((__start, __Symbol::NtProgram(__nt), __end));
                5
            }
            11 => {
                // Program = Stmts => ActionFn(18);
                let __sym0 = __pop_NtStmts(__symbols);
                let __start = __sym0.0.clone();
                let __end = __sym0.2.clone();
                let __nt = super::__action18::<>(__sym0);
                let __states_len = __states.len();
                __states.truncate(__states_len - 1);
                __symbols.push((__start, __Symbol::NtProgram(__nt), __end));
                5
            }
            12 => {
                // Stmt = "Colon" => ActionFn(2);
                let __sym0 = __pop_Term_22Colon_22(__symbols);
                let __start = __sym0.0.clone();
                let __end = __sym0.2.clone();
                let __nt = super::__action2::<>(__sym0);
                let __states_len = __states.len();
                __states.truncate(__states_len - 1);
                __symbols.push((__start, __Symbol::NtStmt(__nt), __end));
                6
            }
            13 => {
                // Stmt? = Stmt => ActionFn(8);
                let __sym0 = __pop_NtStmt(__symbols);
                let __start = __sym0.0.clone();
                let __end = __sym0.2.clone();
                let __nt = super::__action8::<>(__sym0);
                let __states_len = __states.len();
                __states.truncate(__states_len - 1);
                __symbols.push((__start, __Symbol::NtStmt_3f(__nt), __end));
                7
            }
            14 => {
                // Stmt? =  => ActionFn(9);
                let __start = __symbols.last().map(|s| s.2.clone()).unwrap_or_default();
                let __end = __lookahead_start.cloned().unwrap_or_else(|| __start.clone());
                let __nt = super::__action9::<>(&__start, &__end);
                let __states_len = __states.len();
                __states.truncate(__states_len - 0);
                __symbols.push((__start, __Symbol::NtStmt_3f(__nt), __end));
                7
            }
            15 => {
                // Stmts = Stmt => ActionFn(23);
                let __sym0 = __pop_NtStmt(__symbols);
                let __start = __sym0.0.clone();
                let __end = __sym0.2.clone();
                let __nt = super::__action23::<>(__sym0);
                let __states_len = __states.len();
                __states.truncate(__states_len - 1);
                __symbols.push((__start, __Symbol::NtStmts(__nt), __end));
                8
            }
            16 => {
                // Stmts =  => ActionFn(24);
                let __start = __symbols.last().map(|s| s.2.clone()).unwrap_or_default();
                let __end = __lookahead_start.cloned().unwrap_or_else(|| __start.clone());
                let __nt = super::__action24::<>(&__start, &__end);
                let __states_len = __states.len();
                __states.truncate(__states_len - 0);
                __symbols.push((__start, __Symbol::NtStmts(__nt), __end));
                8
            }
            17 => {
                // Stmts = (<Stmt> "Newline")+, Stmt => ActionFn(25);
                let __sym1 = __pop_NtStmt(__symbols);
                let __sym0 = __pop_Nt_28_3cStmt_3e_20_22Newline_22_29_2b(__symbols);
                let __start = __sym0.0.clone();
                let __end = __sym1.2.clone();
                let __nt = super::__action25::<>(__sym0, __sym1);
                let __states_len = __states.len();
                __states.truncate(__states_len - 2);
                __symbols.push((__start, __Symbol::NtStmts(__nt), __end));
                8
            }
            18 => {
                // Stmts = (<Stmt> "Newline")+ => ActionFn(26);
                let __sym0 = __pop_Nt_28_3cStmt_3e_20_22Newline_22_29_2b(__symbols);
                let __start = __sym0.0.clone();
                let __end = __sym0.2.clone();
                let __nt = super::__action26::<>(__sym0);
                let __states_len = __states.len();
                __states.truncate(__states_len - 1);
                __symbols.push((__start, __Symbol::NtStmts(__nt), __end));
                8
            }
            19 => {
                // __Line = Line => ActionFn(0);
                let __sym0 = __pop_NtLine(__symbols);
                let __start = __sym0.0.clone();
                let __end = __sym0.2.clone();
                let __nt = super::__action0::<>(__sym0);
                return Some(Ok(__nt));
            }
            20 => {
                // __Program = Program => ActionFn(1);
                let __sym0 = __pop_NtProgram(__symbols);
                let __start = __sym0.0.clone();
                let __end = __sym0.2.clone();
                let __nt = super::__action1::<>(__sym0);
                let __states_len = __states.len();
                __states.truncate(__states_len - 1);
                __symbols.push((__start, __Symbol::Nt____Program(__nt), __end));
                10
            }
            _ => panic!("invalid action code {}", __action)
        };
        let __state = *__states.last().unwrap() as usize;
        let __next_state = __GOTO[__state * 11 + __nonterminal] - 1;
        __states.push(__next_state);
        None
    }
    fn __pop_Term_22_28_22<
      'input,
    >(
        __symbols: &mut ::std::vec::Vec<(usize,__Symbol<'input>,usize)>
    ) -> (usize, Token<'input>, usize)
     {
        match __symbols.pop().unwrap() {
            (__l, __Symbol::Term_22_28_22(__v), __r) => (__l, __v, __r),
            _ => panic!("symbol type mismatch")
        }
    }
    fn __pop_Term_22_29_22<
      'input,
    >(
        __symbols: &mut ::std::vec::Vec<(usize,__Symbol<'input>,usize)>
    ) -> (usize, Token<'input>, usize)
     {
        match __symbols.pop().unwrap() {
            (__l, __Symbol::Term_22_29_22(__v), __r) => (__l, __v, __r),
            _ => panic!("symbol type mismatch")
        }
    }
    fn __pop_Term_22Colon_22<
      'input,
    >(
        __symbols: &mut ::std::vec::Vec<(usize,__Symbol<'input>,usize)>
    ) -> (usize, &'input str, usize)
     {
        match __symbols.pop().unwrap() {
            (__l, __Symbol::Term_22Colon_22(__v), __r) => (__l, __v, __r),
            _ => panic!("symbol type mismatch")
        }
    }
    fn __pop_Term_22EOF_22<
      'input,
    >(
        __symbols: &mut ::std::vec::Vec<(usize,__Symbol<'input>,usize)>
    ) -> (usize, Token<'input>, usize)
     {
        match __symbols.pop().unwrap() {
            (__l, __Symbol::Term_22EOF_22(__v), __r) => (__l, __v, __r),
            _ => panic!("symbol type mismatch")
        }
    }
    fn __pop_Term_22Newline_22<
      'input,
    >(
        __symbols: &mut ::std::vec::Vec<(usize,__Symbol<'input>,usize)>
    ) -> (usize, Token<'input>, usize)
     {
        match __symbols.pop().unwrap() {
            (__l, __Symbol::Term_22Newline_22(__v), __r) => (__l, __v, __r),
            _ => panic!("symbol type mismatch")
        }
    }
    fn __pop_Nt_22EOF_22_3f<
      'input,
    >(
        __symbols: &mut ::std::vec::Vec<(usize,__Symbol<'input>,usize)>
    ) -> (usize, ::std::option::Option<Token<'input>>, usize)
     {
        match __symbols.pop().unwrap() {
            (__l, __Symbol::Nt_22EOF_22_3f(__v), __r) => (__l, __v, __r),
            _ => panic!("symbol type mismatch")
        }
    }
    fn __pop_Nt_28_3cStmt_3e_20_22Newline_22_29<
      'input,
    >(
        __symbols: &mut ::std::vec::Vec<(usize,__Symbol<'input>,usize)>
    ) -> (usize, Stmt, usize)
     {
        match __symbols.pop().unwrap() {
            (__l, __Symbol::Nt_28_3cStmt_3e_20_22Newline_22_29(__v), __r) => (__l, __v, __r),
            _ => panic!("symbol type mismatch")
        }
    }
    fn __pop_Nt_28_3cStmt_3e_20_22Newline_22_29_2a<
      'input,
    >(
        __symbols: &mut ::std::vec::Vec<(usize,__Symbol<'input>,usize)>
    ) -> (usize, ::std::vec::Vec<Stmt>, usize)
     {
        match __symbols.pop().unwrap() {
            (__l, __Symbol::Nt_28_3cStmt_3e_20_22Newline_22_29_2a(__v), __r) => (__l, __v, __r),
            _ => panic!("symbol type mismatch")
        }
    }
    fn __pop_Nt_28_3cStmt_3e_20_22Newline_22_29_2b<
      'input,
    >(
        __symbols: &mut ::std::vec::Vec<(usize,__Symbol<'input>,usize)>
    ) -> (usize, ::std::vec::Vec<Stmt>, usize)
     {
        match __symbols.pop().unwrap() {
            (__l, __Symbol::Nt_28_3cStmt_3e_20_22Newline_22_29_2b(__v), __r) => (__l, __v, __r),
            _ => panic!("symbol type mismatch")
        }
    }
    fn __pop_NtLine<
      'input,
    >(
        __symbols: &mut ::std::vec::Vec<(usize,__Symbol<'input>,usize)>
    ) -> (usize, Stmt, usize)
     {
        match __symbols.pop().unwrap() {
            (__l, __Symbol::NtLine(__v), __r) => (__l, __v, __r),
            _ => panic!("symbol type mismatch")
        }
    }
    fn __pop_NtProgram<
      'input,
    >(
        __symbols: &mut ::std::vec::Vec<(usize,__Symbol<'input>,usize)>
    ) -> (usize, Program, usize)
     {
        match __symbols.pop().unwrap() {
            (__l, __Symbol::NtProgram(__v), __r) => (__l, __v, __r),
            _ => panic!("symbol type mismatch")
        }
    }
    fn __pop_NtStmt<
      'input,
    >(
        __symbols: &mut ::std::vec::Vec<(usize,__Symbol<'input>,usize)>
    ) -> (usize, Stmt, usize)
     {
        match __symbols.pop().unwrap() {
            (__l, __Symbol::NtStmt(__v), __r) => (__l, __v, __r),
            _ => panic!("symbol type mismatch")
        }
    }
    fn __pop_NtStmt_3f<
      'input,
    >(
        __symbols: &mut ::std::vec::Vec<(usize,__Symbol<'input>,usize)>
    ) -> (usize, ::std::option::Option<Stmt>, usize)
     {
        match __symbols.pop().unwrap() {
            (__l, __Symbol::NtStmt_3f(__v), __r) => (__l, __v, __r),
            _ => panic!("symbol type mismatch")
        }
    }
    fn __pop_NtStmts<
      'input,
    >(
        __symbols: &mut ::std::vec::Vec<(usize,__Symbol<'input>,usize)>
    ) -> (usize, Vec<Stmt>, usize)
     {
        match __symbols.pop().unwrap() {
            (__l, __Symbol::NtStmts(__v), __r) => (__l, __v, __r),
            _ => panic!("symbol type mismatch")
        }
    }
    fn __pop_Nt____Line<
      'input,
    >(
        __symbols: &mut ::std::vec::Vec<(usize,__Symbol<'input>,usize)>
    ) -> (usize, Stmt, usize)
     {
        match __symbols.pop().unwrap() {
            (__l, __Symbol::Nt____Line(__v), __r) => (__l, __v, __r),
            _ => panic!("symbol type mismatch")
        }
    }
    fn __pop_Nt____Program<
      'input,
    >(
        __symbols: &mut ::std::vec::Vec<(usize,__Symbol<'input>,usize)>
    ) -> (usize, Program, usize)
     {
        match __symbols.pop().unwrap() {
            (__l, __Symbol::Nt____Program(__v), __r) => (__l, __v, __r),
            _ => panic!("symbol type mismatch")
        }
    }
}
pub use self::__parse__Line::parse_Line;

mod __parse__Program {
    #![allow(non_snake_case, non_camel_case_types, unused_mut, unused_variables, unused_imports, unused_parens)]

    use ast::{Expr, Program, Stmt};
    use lexer::{LexError, Token};
    #[allow(unused_extern_crates)]
    extern crate lalrpop_util as __lalrpop_util;
    use super::__ToTriple;
    #[allow(dead_code)]
    pub enum __Symbol<'input>
     {
        Term_22_28_22(Token<'input>),
        Term_22_29_22(Token<'input>),
        Term_22Colon_22(&'input str),
        Term_22EOF_22(Token<'input>),
        Term_22Newline_22(Token<'input>),
        Nt_22EOF_22_3f(::std::option::Option<Token<'input>>),
        Nt_28_3cStmt_3e_20_22Newline_22_29(Stmt),
        Nt_28_3cStmt_3e_20_22Newline_22_29_2a(::std::vec::Vec<Stmt>),
        Nt_28_3cStmt_3e_20_22Newline_22_29_2b(::std::vec::Vec<Stmt>),
        NtLine(Stmt),
        NtProgram(Program),
        NtStmt(Stmt),
        NtStmt_3f(::std::option::Option<Stmt>),
        NtStmts(Vec<Stmt>),
        Nt____Line(Stmt),
        Nt____Program(Program),
    }
    const __ACTION: &'static [i32] = &[
        // State 0
        0, 0, 6, -16, 0,
        // State 1
        0, 0, 6, -18, 0,
        // State 2
        0, 0, 0, 0, 0,
        // State 3
        0, 0, 0, -15, 8,
        // State 4
        0, 0, 0, 9, 0,
        // State 5
        0, 0, 0, -12, -12,
        // State 6
        0, 0, 0, -17, 10,
        // State 7
        0, 0, -6, -6, 0,
        // State 8
        0, 0, 0, 0, 0,
        // State 9
        0, 0, -7, -7, 0,
    ];
    const __EOF_ACTION: &'static [i32] = &[
        // State 0
        -16,
        // State 1
        -18,
        // State 2
        -20,
        // State 3
        -15,
        // State 4
        -11,
        // State 5
        -12,
        // State 6
        -17,
        // State 7
        -6,
        // State 8
        -10,
        // State 9
        -7,
    ];
    const __GOTO: &'static [i32] = &[
        // State 0
        0, 0, 0, 2, 0, 3, 4, 0, 5, 0, 0,
        // State 1
        0, 0, 0, 0, 0, 0, 7, 0, 0, 0, 0,
        // State 2
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        // State 3
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        // State 4
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        // State 5
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        // State 6
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        // State 7
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        // State 8
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        // State 9
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    ];
    fn __expected_tokens(__state: usize) -> Vec<::std::string::String> {
        const __TERMINAL: &'static [&'static str] = &[
            r###""(""###,
            r###"")""###,
            r###""Colon""###,
            r###""EOF""###,
            r###""Newline""###,
        ];
        __ACTION[(__state * 5)..].iter().zip(__TERMINAL).filter_map(|(&state, terminal)| {
            if state == 0 {
                None
            } else {
                Some(terminal.to_string())
            }
        }).collect()
    }
    #[allow(dead_code)]
    pub fn parse_Program<
        'input,
        __TOKEN: __ToTriple<'input, Error=LexError>,
        __TOKENS: IntoIterator<Item=__TOKEN>,
    >(
        __tokens0: __TOKENS,
    ) -> Result<Program, __lalrpop_util::ParseError<usize, Token<'input>, LexError>>
    {
        let __tokens = __tokens0.into_iter();
        let mut __tokens = __tokens.map(|t| __ToTriple::to_triple(t));
        let mut __states = vec![0_i32];
        let mut __symbols = vec![];
        let mut __integer;
        let mut __lookahead;
        let __last_location = &mut Default::default();
        '__shift: loop {
            __lookahead = match __tokens.next() {
                Some(Ok(v)) => v,
                None => break '__shift,
                Some(Err(e)) => return Err(__lalrpop_util::ParseError::User { error: e }),
            };
            *__last_location = __lookahead.2.clone();
            __integer = match __lookahead.1 {
                Token::LeftParen if true => 0,
                Token::RightParen if true => 1,
                Token::Symbol(_) if true => 2,
                Token::EOF if true => 3,
                Token::Newline if true => 4,
                _ => {
                    let __state = *__states.last().unwrap() as usize;
                    let __error = __lalrpop_util::ParseError::UnrecognizedToken {
                        token: Some(__lookahead),
                        expected: __expected_tokens(__state),
                    };
                    return Err(__error);
                }
            };
            '__inner: loop {
                let __state = *__states.last().unwrap() as usize;
                let __action = __ACTION[__state * 5 + __integer];
                if __action > 0 {
                    let __symbol = match __integer {
                        0 => match __lookahead.1 {
                            __tok @ Token::LeftParen => __Symbol::Term_22_28_22((__tok)),
                            _ => unreachable!(),
                        },
                        1 => match __lookahead.1 {
                            __tok @ Token::RightParen => __Symbol::Term_22_29_22((__tok)),
                            _ => unreachable!(),
                        },
                        2 => match __lookahead.1 {
                            Token::Symbol(__tok0) => __Symbol::Term_22Colon_22((__tok0)),
                            _ => unreachable!(),
                        },
                        3 => match __lookahead.1 {
                            __tok @ Token::EOF => __Symbol::Term_22EOF_22((__tok)),
                            _ => unreachable!(),
                        },
                        4 => match __lookahead.1 {
                            __tok @ Token::Newline => __Symbol::Term_22Newline_22((__tok)),
                            _ => unreachable!(),
                        },
                        _ => unreachable!(),
                    };
                    __states.push(__action - 1);
                    __symbols.push((__lookahead.0, __symbol, __lookahead.2));
                    continue '__shift;
                } else if __action < 0 {
                    if let Some(r) = __reduce(__action, Some(&__lookahead.0), &mut __states, &mut __symbols, ::std::marker::PhantomData::<()>) {
                        if r.is_err() {
                            return r;
                        }
                        return Err(__lalrpop_util::ParseError::ExtraToken { token: __lookahead });
                    }
                } else {
                    let mut __err_lookahead = Some(__lookahead);
                    let mut __err_integer: Option<usize> = Some(__integer);
                    let __state = *__states.last().unwrap() as usize;
                    let __error = __lalrpop_util::ParseError::UnrecognizedToken {
                        token: __err_lookahead,
                        expected: __expected_tokens(__state),
                    };
                    return Err(__error)
                }
            }
        }
        loop {
            let __state = *__states.last().unwrap() as usize;
            let __action = __EOF_ACTION[__state];
            if __action < 0 {
                if let Some(r) = __reduce(__action, None, &mut __states, &mut __symbols, ::std::marker::PhantomData::<()>) {
                    return r;
                }
            } else {
                let mut __err_lookahead = None;
                let mut __err_integer: Option<usize> = None;
                let __state = *__states.last().unwrap() as usize;
                let __error = __lalrpop_util::ParseError::UnrecognizedToken {
                    token: __err_lookahead,
                    expected: __expected_tokens(__state),
                };
                return Err(__error)
            }
        }
    }
    pub fn __reduce<
        'input,
    >(
        __action: i32,
        __lookahead_start: Option<&usize>,
        __states: &mut ::std::vec::Vec<i32>,
        __symbols: &mut ::std::vec::Vec<(usize,__Symbol<'input>,usize)>,
        _: ::std::marker::PhantomData<()>,
    ) -> Option<Result<Program,__lalrpop_util::ParseError<usize, Token<'input>, LexError>>>
    {
        let __nonterminal = match -__action {
            1 => {
                // "EOF"? = "EOF" => ActionFn(6);
                let __sym0 = __pop_Term_22EOF_22(__symbols);
                let __start = __sym0.0.clone();
                let __end = __sym0.2.clone();
                let __nt = super::__action6::<>(__sym0);
                let __states_len = __states.len();
                __states.truncate(__states_len - 1);
                __symbols.push((__start, __Symbol::Nt_22EOF_22_3f(__nt), __end));
                0
            }
            2 => {
                // "EOF"? =  => ActionFn(7);
                let __start = __symbols.last().map(|s| s.2.clone()).unwrap_or_default();
                let __end = __lookahead_start.cloned().unwrap_or_else(|| __start.clone());
                let __nt = super::__action7::<>(&__start, &__end);
                let __states_len = __states.len();
                __states.truncate(__states_len - 0);
                __symbols.push((__start, __Symbol::Nt_22EOF_22_3f(__nt), __end));
                0
            }
            3 => {
                // (<Stmt> "Newline") = Stmt, "Newline" => ActionFn(12);
                let __sym1 = __pop_Term_22Newline_22(__symbols);
                let __sym0 = __pop_NtStmt(__symbols);
                let __start = __sym0.0.clone();
                let __end = __sym1.2.clone();
                let __nt = super::__action12::<>(__sym0, __sym1);
                let __states_len = __states.len();
                __states.truncate(__states_len - 2);
                __symbols.push((__start, __Symbol::Nt_28_3cStmt_3e_20_22Newline_22_29(__nt), __end));
                1
            }
            4 => {
                // (<Stmt> "Newline")* =  => ActionFn(10);
                let __start = __symbols.last().map(|s| s.2.clone()).unwrap_or_default();
                let __end = __lookahead_start.cloned().unwrap_or_else(|| __start.clone());
                let __nt = super::__action10::<>(&__start, &__end);
                let __states_len = __states.len();
                __states.truncate(__states_len - 0);
                __symbols.push((__start, __Symbol::Nt_28_3cStmt_3e_20_22Newline_22_29_2a(__nt), __end));
                2
            }
            5 => {
                // (<Stmt> "Newline")* = (<Stmt> "Newline")+ => ActionFn(11);
                let __sym0 = __pop_Nt_28_3cStmt_3e_20_22Newline_22_29_2b(__symbols);
                let __start = __sym0.0.clone();
                let __end = __sym0.2.clone();
                let __nt = super::__action11::<>(__sym0);
                let __states_len = __states.len();
                __states.truncate(__states_len - 1);
                __symbols.push((__start, __Symbol::Nt_28_3cStmt_3e_20_22Newline_22_29_2a(__nt), __end));
                2
            }
            6 => {
                // (<Stmt> "Newline")+ = Stmt, "Newline" => ActionFn(19);
                let __sym1 = __pop_Term_22Newline_22(__symbols);
                let __sym0 = __pop_NtStmt(__symbols);
                let __start = __sym0.0.clone();
                let __end = __sym1.2.clone();
                let __nt = super::__action19::<>(__sym0, __sym1);
                let __states_len = __states.len();
                __states.truncate(__states_len - 2);
                __symbols.push((__start, __Symbol::Nt_28_3cStmt_3e_20_22Newline_22_29_2b(__nt), __end));
                3
            }
            7 => {
                // (<Stmt> "Newline")+ = (<Stmt> "Newline")+, Stmt, "Newline" => ActionFn(20);
                let __sym2 = __pop_Term_22Newline_22(__symbols);
                let __sym1 = __pop_NtStmt(__symbols);
                let __sym0 = __pop_Nt_28_3cStmt_3e_20_22Newline_22_29_2b(__symbols);
                let __start = __sym0.0.clone();
                let __end = __sym2.2.clone();
                let __nt = super::__action20::<>(__sym0, __sym1, __sym2);
                let __states_len = __states.len();
                __states.truncate(__states_len - 3);
                __symbols.push((__start, __Symbol::Nt_28_3cStmt_3e_20_22Newline_22_29_2b(__nt), __end));
                3
            }
            8 => {
                // Line = Stmt, "EOF" => ActionFn(15);
                let __sym1 = __pop_Term_22EOF_22(__symbols);
                let __sym0 = __pop_NtStmt(__symbols);
                let __start = __sym0.0.clone();
                let __end = __sym1.2.clone();
                let __nt = super::__action15::<>(__sym0, __sym1);
                let __states_len = __states.len();
                __states.truncate(__states_len - 2);
                __symbols.push((__start, __Symbol::NtLine(__nt), __end));
                4
            }
            9 => {
                // Line = Stmt => ActionFn(16);
                let __sym0 = __pop_NtStmt(__symbols);
                let __start = __sym0.0.clone();
                let __end = __sym0.2.clone();
                let __nt = super::__action16::<>(__sym0);
                let __states_len = __states.len();
                __states.truncate(__states_len - 1);
                __symbols.push((__start, __Symbol::NtLine(__nt), __end));
                4
            }
            10 => {
                // Program = Stmts, "EOF" => ActionFn(17);
                let __sym1 = __pop_Term_22EOF_22(__symbols);
                let __sym0 = __pop_NtStmts(__symbols);
                let __start = __sym0.0.clone();
                let __end = __sym1.2.clone();
                let __nt = super::__action17::<>(__sym0, __sym1);
                let __states_len = __states.len();
                __states.truncate(__states_len - 2);
                __symbols.push((__start, __Symbol::NtProgram(__nt), __end));
                5
            }
            11 => {
                // Program = Stmts => ActionFn(18);
                let __sym0 = __pop_NtStmts(__symbols);
                let __start = __sym0.0.clone();
                let __end = __sym0.2.clone();
                let __nt = super::__action18::<>(__sym0);
                let __states_len = __states.len();
                __states.truncate(__states_len - 1);
                __symbols.push((__start, __Symbol::NtProgram(__nt), __end));
                5
            }
            12 => {
                // Stmt = "Colon" => ActionFn(2);
                let __sym0 = __pop_Term_22Colon_22(__symbols);
                let __start = __sym0.0.clone();
                let __end = __sym0.2.clone();
                let __nt = super::__action2::<>(__sym0);
                let __states_len = __states.len();
                __states.truncate(__states_len - 1);
                __symbols.push((__start, __Symbol::NtStmt(__nt), __end));
                6
            }
            13 => {
                // Stmt? = Stmt => ActionFn(8);
                let __sym0 = __pop_NtStmt(__symbols);
                let __start = __sym0.0.clone();
                let __end = __sym0.2.clone();
                let __nt = super::__action8::<>(__sym0);
                let __states_len = __states.len();
                __states.truncate(__states_len - 1);
                __symbols.push((__start, __Symbol::NtStmt_3f(__nt), __end));
                7
            }
            14 => {
                // Stmt? =  => ActionFn(9);
                let __start = __symbols.last().map(|s| s.2.clone()).unwrap_or_default();
                let __end = __lookahead_start.cloned().unwrap_or_else(|| __start.clone());
                let __nt = super::__action9::<>(&__start, &__end);
                let __states_len = __states.len();
                __states.truncate(__states_len - 0);
                __symbols.push((__start, __Symbol::NtStmt_3f(__nt), __end));
                7
            }
            15 => {
                // Stmts = Stmt => ActionFn(23);
                let __sym0 = __pop_NtStmt(__symbols);
                let __start = __sym0.0.clone();
                let __end = __sym0.2.clone();
                let __nt = super::__action23::<>(__sym0);
                let __states_len = __states.len();
                __states.truncate(__states_len - 1);
                __symbols.push((__start, __Symbol::NtStmts(__nt), __end));
                8
            }
            16 => {
                // Stmts =  => ActionFn(24);
                let __start = __symbols.last().map(|s| s.2.clone()).unwrap_or_default();
                let __end = __lookahead_start.cloned().unwrap_or_else(|| __start.clone());
                let __nt = super::__action24::<>(&__start, &__end);
                let __states_len = __states.len();
                __states.truncate(__states_len - 0);
                __symbols.push((__start, __Symbol::NtStmts(__nt), __end));
                8
            }
            17 => {
                // Stmts = (<Stmt> "Newline")+, Stmt => ActionFn(25);
                let __sym1 = __pop_NtStmt(__symbols);
                let __sym0 = __pop_Nt_28_3cStmt_3e_20_22Newline_22_29_2b(__symbols);
                let __start = __sym0.0.clone();
                let __end = __sym1.2.clone();
                let __nt = super::__action25::<>(__sym0, __sym1);
                let __states_len = __states.len();
                __states.truncate(__states_len - 2);
                __symbols.push((__start, __Symbol::NtStmts(__nt), __end));
                8
            }
            18 => {
                // Stmts = (<Stmt> "Newline")+ => ActionFn(26);
                let __sym0 = __pop_Nt_28_3cStmt_3e_20_22Newline_22_29_2b(__symbols);
                let __start = __sym0.0.clone();
                let __end = __sym0.2.clone();
                let __nt = super::__action26::<>(__sym0);
                let __states_len = __states.len();
                __states.truncate(__states_len - 1);
                __symbols.push((__start, __Symbol::NtStmts(__nt), __end));
                8
            }
            19 => {
                // __Line = Line => ActionFn(0);
                let __sym0 = __pop_NtLine(__symbols);
                let __start = __sym0.0.clone();
                let __end = __sym0.2.clone();
                let __nt = super::__action0::<>(__sym0);
                let __states_len = __states.len();
                __states.truncate(__states_len - 1);
                __symbols.push((__start, __Symbol::Nt____Line(__nt), __end));
                9
            }
            20 => {
                // __Program = Program => ActionFn(1);
                let __sym0 = __pop_NtProgram(__symbols);
                let __start = __sym0.0.clone();
                let __end = __sym0.2.clone();
                let __nt = super::__action1::<>(__sym0);
                return Some(Ok(__nt));
            }
            _ => panic!("invalid action code {}", __action)
        };
        let __state = *__states.last().unwrap() as usize;
        let __next_state = __GOTO[__state * 11 + __nonterminal] - 1;
        __states.push(__next_state);
        None
    }
    fn __pop_Term_22_28_22<
      'input,
    >(
        __symbols: &mut ::std::vec::Vec<(usize,__Symbol<'input>,usize)>
    ) -> (usize, Token<'input>, usize)
     {
        match __symbols.pop().unwrap() {
            (__l, __Symbol::Term_22_28_22(__v), __r) => (__l, __v, __r),
            _ => panic!("symbol type mismatch")
        }
    }
    fn __pop_Term_22_29_22<
      'input,
    >(
        __symbols: &mut ::std::vec::Vec<(usize,__Symbol<'input>,usize)>
    ) -> (usize, Token<'input>, usize)
     {
        match __symbols.pop().unwrap() {
            (__l, __Symbol::Term_22_29_22(__v), __r) => (__l, __v, __r),
            _ => panic!("symbol type mismatch")
        }
    }
    fn __pop_Term_22Colon_22<
      'input,
    >(
        __symbols: &mut ::std::vec::Vec<(usize,__Symbol<'input>,usize)>
    ) -> (usize, &'input str, usize)
     {
        match __symbols.pop().unwrap() {
            (__l, __Symbol::Term_22Colon_22(__v), __r) => (__l, __v, __r),
            _ => panic!("symbol type mismatch")
        }
    }
    fn __pop_Term_22EOF_22<
      'input,
    >(
        __symbols: &mut ::std::vec::Vec<(usize,__Symbol<'input>,usize)>
    ) -> (usize, Token<'input>, usize)
     {
        match __symbols.pop().unwrap() {
            (__l, __Symbol::Term_22EOF_22(__v), __r) => (__l, __v, __r),
            _ => panic!("symbol type mismatch")
        }
    }
    fn __pop_Term_22Newline_22<
      'input,
    >(
        __symbols: &mut ::std::vec::Vec<(usize,__Symbol<'input>,usize)>
    ) -> (usize, Token<'input>, usize)
     {
        match __symbols.pop().unwrap() {
            (__l, __Symbol::Term_22Newline_22(__v), __r) => (__l, __v, __r),
            _ => panic!("symbol type mismatch")
        }
    }
    fn __pop_Nt_22EOF_22_3f<
      'input,
    >(
        __symbols: &mut ::std::vec::Vec<(usize,__Symbol<'input>,usize)>
    ) -> (usize, ::std::option::Option<Token<'input>>, usize)
     {
        match __symbols.pop().unwrap() {
            (__l, __Symbol::Nt_22EOF_22_3f(__v), __r) => (__l, __v, __r),
            _ => panic!("symbol type mismatch")
        }
    }
    fn __pop_Nt_28_3cStmt_3e_20_22Newline_22_29<
      'input,
    >(
        __symbols: &mut ::std::vec::Vec<(usize,__Symbol<'input>,usize)>
    ) -> (usize, Stmt, usize)
     {
        match __symbols.pop().unwrap() {
            (__l, __Symbol::Nt_28_3cStmt_3e_20_22Newline_22_29(__v), __r) => (__l, __v, __r),
            _ => panic!("symbol type mismatch")
        }
    }
    fn __pop_Nt_28_3cStmt_3e_20_22Newline_22_29_2a<
      'input,
    >(
        __symbols: &mut ::std::vec::Vec<(usize,__Symbol<'input>,usize)>
    ) -> (usize, ::std::vec::Vec<Stmt>, usize)
     {
        match __symbols.pop().unwrap() {
            (__l, __Symbol::Nt_28_3cStmt_3e_20_22Newline_22_29_2a(__v), __r) => (__l, __v, __r),
            _ => panic!("symbol type mismatch")
        }
    }
    fn __pop_Nt_28_3cStmt_3e_20_22Newline_22_29_2b<
      'input,
    >(
        __symbols: &mut ::std::vec::Vec<(usize,__Symbol<'input>,usize)>
    ) -> (usize, ::std::vec::Vec<Stmt>, usize)
     {
        match __symbols.pop().unwrap() {
            (__l, __Symbol::Nt_28_3cStmt_3e_20_22Newline_22_29_2b(__v), __r) => (__l, __v, __r),
            _ => panic!("symbol type mismatch")
        }
    }
    fn __pop_NtLine<
      'input,
    >(
        __symbols: &mut ::std::vec::Vec<(usize,__Symbol<'input>,usize)>
    ) -> (usize, Stmt, usize)
     {
        match __symbols.pop().unwrap() {
            (__l, __Symbol::NtLine(__v), __r) => (__l, __v, __r),
            _ => panic!("symbol type mismatch")
        }
    }
    fn __pop_NtProgram<
      'input,
    >(
        __symbols: &mut ::std::vec::Vec<(usize,__Symbol<'input>,usize)>
    ) -> (usize, Program, usize)
     {
        match __symbols.pop().unwrap() {
            (__l, __Symbol::NtProgram(__v), __r) => (__l, __v, __r),
            _ => panic!("symbol type mismatch")
        }
    }
    fn __pop_NtStmt<
      'input,
    >(
        __symbols: &mut ::std::vec::Vec<(usize,__Symbol<'input>,usize)>
    ) -> (usize, Stmt, usize)
     {
        match __symbols.pop().unwrap() {
            (__l, __Symbol::NtStmt(__v), __r) => (__l, __v, __r),
            _ => panic!("symbol type mismatch")
        }
    }
    fn __pop_NtStmt_3f<
      'input,
    >(
        __symbols: &mut ::std::vec::Vec<(usize,__Symbol<'input>,usize)>
    ) -> (usize, ::std::option::Option<Stmt>, usize)
     {
        match __symbols.pop().unwrap() {
            (__l, __Symbol::NtStmt_3f(__v), __r) => (__l, __v, __r),
            _ => panic!("symbol type mismatch")
        }
    }
    fn __pop_NtStmts<
      'input,
    >(
        __symbols: &mut ::std::vec::Vec<(usize,__Symbol<'input>,usize)>
    ) -> (usize, Vec<Stmt>, usize)
     {
        match __symbols.pop().unwrap() {
            (__l, __Symbol::NtStmts(__v), __r) => (__l, __v, __r),
            _ => panic!("symbol type mismatch")
        }
    }
    fn __pop_Nt____Line<
      'input,
    >(
        __symbols: &mut ::std::vec::Vec<(usize,__Symbol<'input>,usize)>
    ) -> (usize, Stmt, usize)
     {
        match __symbols.pop().unwrap() {
            (__l, __Symbol::Nt____Line(__v), __r) => (__l, __v, __r),
            _ => panic!("symbol type mismatch")
        }
    }
    fn __pop_Nt____Program<
      'input,
    >(
        __symbols: &mut ::std::vec::Vec<(usize,__Symbol<'input>,usize)>
    ) -> (usize, Program, usize)
     {
        match __symbols.pop().unwrap() {
            (__l, __Symbol::Nt____Program(__v), __r) => (__l, __v, __r),
            _ => panic!("symbol type mismatch")
        }
    }
}
pub use self::__parse__Program::parse_Program;

fn __action0<
    'input,
>(
    (_, __0, _): (usize, Stmt, usize),
) -> Stmt
{
    (__0)
}

fn __action1<
    'input,
>(
    (_, __0, _): (usize, Program, usize),
) -> Program
{
    (__0)
}

fn __action2<
    'input,
>(
    (_, __0, _): (usize, &'input str, usize),
) -> Stmt
{
    Stmt::Expr(Expr::IntLiteral(1))
}

fn __action3<
    'input,
>(
    (_, v0, _): (usize, ::std::vec::Vec<Stmt>, usize),
    (_, e1, _): (usize, ::std::option::Option<Stmt>, usize),
) -> Vec<Stmt>
{
    v0.into_iter().chain(e1).collect()
}

fn __action4<
    'input,
>(
    (_, s, _): (usize, Stmt, usize),
    (_, x, _): (usize, ::std::option::Option<Token<'input>>, usize),
) -> Stmt
{
    s
}

fn __action5<
    'input,
>(
    (_, v, _): (usize, Vec<Stmt>, usize),
    (_, x, _): (usize, ::std::option::Option<Token<'input>>, usize),
) -> Program
{
    Program {}
}

fn __action6<
    'input,
>(
    (_, __0, _): (usize, Token<'input>, usize),
) -> ::std::option::Option<Token<'input>>
{
    Some(__0)
}

fn __action7<
    'input,
>(
    __lookbehind: &usize,
    __lookahead: &usize,
) -> ::std::option::Option<Token<'input>>
{
    None
}

fn __action8<
    'input,
>(
    (_, __0, _): (usize, Stmt, usize),
) -> ::std::option::Option<Stmt>
{
    Some(__0)
}

fn __action9<
    'input,
>(
    __lookbehind: &usize,
    __lookahead: &usize,
) -> ::std::option::Option<Stmt>
{
    None
}

fn __action10<
    'input,
>(
    __lookbehind: &usize,
    __lookahead: &usize,
) -> ::std::vec::Vec<Stmt>
{
    vec![]
}

fn __action11<
    'input,
>(
    (_, v, _): (usize, ::std::vec::Vec<Stmt>, usize),
) -> ::std::vec::Vec<Stmt>
{
    v
}

fn __action12<
    'input,
>(
    (_, __0, _): (usize, Stmt, usize),
    (_, _, _): (usize, Token<'input>, usize),
) -> Stmt
{
    (__0)
}

fn __action13<
    'input,
>(
    (_, __0, _): (usize, Stmt, usize),
) -> ::std::vec::Vec<Stmt>
{
    vec![__0]
}

fn __action14<
    'input,
>(
    (_, v, _): (usize, ::std::vec::Vec<Stmt>, usize),
    (_, e, _): (usize, Stmt, usize),
) -> ::std::vec::Vec<Stmt>
{
    { let mut v = v; v.push(e); v }
}

fn __action15<
    'input,
>(
    __0: (usize, Stmt, usize),
    __1: (usize, Token<'input>, usize),
) -> Stmt
{
    let __start0 = __1.0.clone();
    let __end0 = __1.2.clone();
    let __temp0 = __action6(
        __1,
    );
    let __temp0 = (__start0, __temp0, __end0);
    __action4(
        __0,
        __temp0,
    )
}

fn __action16<
    'input,
>(
    __0: (usize, Stmt, usize),
) -> Stmt
{
    let __start0 = __0.2.clone();
    let __end0 = __0.2.clone();
    let __temp0 = __action7(
        &__start0,
        &__end0,
    );
    let __temp0 = (__start0, __temp0, __end0);
    __action4(
        __0,
        __temp0,
    )
}

fn __action17<
    'input,
>(
    __0: (usize, Vec<Stmt>, usize),
    __1: (usize, Token<'input>, usize),
) -> Program
{
    let __start0 = __1.0.clone();
    let __end0 = __1.2.clone();
    let __temp0 = __action6(
        __1,
    );
    let __temp0 = (__start0, __temp0, __end0);
    __action5(
        __0,
        __temp0,
    )
}

fn __action18<
    'input,
>(
    __0: (usize, Vec<Stmt>, usize),
) -> Program
{
    let __start0 = __0.2.clone();
    let __end0 = __0.2.clone();
    let __temp0 = __action7(
        &__start0,
        &__end0,
    );
    let __temp0 = (__start0, __temp0, __end0);
    __action5(
        __0,
        __temp0,
    )
}

fn __action19<
    'input,
>(
    __0: (usize, Stmt, usize),
    __1: (usize, Token<'input>, usize),
) -> ::std::vec::Vec<Stmt>
{
    let __start0 = __0.0.clone();
    let __end0 = __1.2.clone();
    let __temp0 = __action12(
        __0,
        __1,
    );
    let __temp0 = (__start0, __temp0, __end0);
    __action13(
        __temp0,
    )
}

fn __action20<
    'input,
>(
    __0: (usize, ::std::vec::Vec<Stmt>, usize),
    __1: (usize, Stmt, usize),
    __2: (usize, Token<'input>, usize),
) -> ::std::vec::Vec<Stmt>
{
    let __start0 = __1.0.clone();
    let __end0 = __2.2.clone();
    let __temp0 = __action12(
        __1,
        __2,
    );
    let __temp0 = (__start0, __temp0, __end0);
    __action14(
        __0,
        __temp0,
    )
}

fn __action21<
    'input,
>(
    __0: (usize, ::std::option::Option<Stmt>, usize),
) -> Vec<Stmt>
{
    let __start0 = __0.0.clone();
    let __end0 = __0.0.clone();
    let __temp0 = __action10(
        &__start0,
        &__end0,
    );
    let __temp0 = (__start0, __temp0, __end0);
    __action3(
        __temp0,
        __0,
    )
}

fn __action22<
    'input,
>(
    __0: (usize, ::std::vec::Vec<Stmt>, usize),
    __1: (usize, ::std::option::Option<Stmt>, usize),
) -> Vec<Stmt>
{
    let __start0 = __0.0.clone();
    let __end0 = __0.2.clone();
    let __temp0 = __action11(
        __0,
    );
    let __temp0 = (__start0, __temp0, __end0);
    __action3(
        __temp0,
        __1,
    )
}

fn __action23<
    'input,
>(
    __0: (usize, Stmt, usize),
) -> Vec<Stmt>
{
    let __start0 = __0.0.clone();
    let __end0 = __0.2.clone();
    let __temp0 = __action8(
        __0,
    );
    let __temp0 = (__start0, __temp0, __end0);
    __action21(
        __temp0,
    )
}

fn __action24<
    'input,
>(
    __lookbehind: &usize,
    __lookahead: &usize,
) -> Vec<Stmt>
{
    let __start0 = __lookbehind.clone();
    let __end0 = __lookahead.clone();
    let __temp0 = __action9(
        &__start0,
        &__end0,
    );
    let __temp0 = (__start0, __temp0, __end0);
    __action21(
        __temp0,
    )
}

fn __action25<
    'input,
>(
    __0: (usize, ::std::vec::Vec<Stmt>, usize),
    __1: (usize, Stmt, usize),
) -> Vec<Stmt>
{
    let __start0 = __1.0.clone();
    let __end0 = __1.2.clone();
    let __temp0 = __action8(
        __1,
    );
    let __temp0 = (__start0, __temp0, __end0);
    __action22(
        __0,
        __temp0,
    )
}

fn __action26<
    'input,
>(
    __0: (usize, ::std::vec::Vec<Stmt>, usize),
) -> Vec<Stmt>
{
    let __start0 = __0.2.clone();
    let __end0 = __0.2.clone();
    let __temp0 = __action9(
        &__start0,
        &__end0,
    );
    let __temp0 = (__start0, __temp0, __end0);
    __action22(
        __0,
        __temp0,
    )
}

pub trait __ToTriple<'input, > {
    type Error;
    fn to_triple(value: Self) -> Result<(usize,Token<'input>,usize),Self::Error>;
}

impl<'input, > __ToTriple<'input, > for (usize, Token<'input>, usize) {
    type Error = LexError;
    fn to_triple(value: Self) -> Result<(usize,Token<'input>,usize),LexError> {
        Ok(value)
    }
}
impl<'input, > __ToTriple<'input, > for Result<(usize, Token<'input>, usize),LexError> {
    type Error = LexError;
    fn to_triple(value: Self) -> Result<(usize,Token<'input>,usize),LexError> {
        value
    }
}
