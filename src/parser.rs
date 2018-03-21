// auto-generated: "lalrpop 0.14.0"
use ast::{Expr, Program, Stmt};
use lexer::{LexError, Token};
#[allow(unused_extern_crates)]
extern crate lalrpop_util as __lalrpop_util;

mod __parse__Program {
    #![allow(non_snake_case, non_camel_case_types, unused_mut, unused_variables, unused_imports, unused_parens)]

    use ast::{Expr, Program, Stmt};
    use lexer::{LexError, Token};
    #[allow(unused_extern_crates)]
    extern crate lalrpop_util as __lalrpop_util;
    use super::__ToTriple;
    #[allow(dead_code)]
    pub enum __Symbol<>
     {
        Term_22_28_22(Token),
        Term_22_29_22(Token),
        Term_22_3a_22(Token),
        NtProgram(Program),
        NtStmt(Stmt),
        NtStmt_2a(::std::vec::Vec<Stmt>),
        NtStmt_2b(::std::vec::Vec<Stmt>),
        Nt____Program(Program),
    }
    const __ACTION: &'static [i32] = &[
        // State 0
        0, 0, 5,
        // State 1
        0, 0, 0,
        // State 2
        0, 0, -6,
        // State 3
        0, 0, 5,
        // State 4
        0, 0, -3,
        // State 5
        0, 0, -7,
    ];
    const __EOF_ACTION: &'static [i32] = &[
        // State 0
        -1,
        // State 1
        -8,
        // State 2
        -6,
        // State 3
        -2,
        // State 4
        -3,
        // State 5
        -7,
    ];
    const __GOTO: &'static [i32] = &[
        // State 0
        2, 3, 0, 4, 0,
        // State 1
        0, 0, 0, 0, 0,
        // State 2
        0, 0, 0, 0, 0,
        // State 3
        0, 6, 0, 0, 0,
        // State 4
        0, 0, 0, 0, 0,
        // State 5
        0, 0, 0, 0, 0,
    ];
    fn __expected_tokens(__state: usize) -> Vec<::std::string::String> {
        const __TERMINAL: &'static [&'static str] = &[
            r###""(""###,
            r###"")""###,
            r###"":""###,
        ];
        __ACTION[(__state * 3)..].iter().zip(__TERMINAL).filter_map(|(&state, terminal)| {
            if state == 0 {
                None
            } else {
                Some(terminal.to_string())
            }
        }).collect()
    }
    #[allow(dead_code)]
    pub fn parse_Program<
        __TOKEN: __ToTriple<Error=LexError>,
        __TOKENS: IntoIterator<Item=__TOKEN>,
    >(
        __tokens0: __TOKENS,
    ) -> Result<Program, __lalrpop_util::ParseError<usize, Token, LexError>>
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
                Token::Colon if true => 2,
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
                let __action = __ACTION[__state * 3 + __integer];
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
                            __tok @ Token::Colon => __Symbol::Term_22_3a_22((__tok)),
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
    >(
        __action: i32,
        __lookahead_start: Option<&usize>,
        __states: &mut ::std::vec::Vec<i32>,
        __symbols: &mut ::std::vec::Vec<(usize,__Symbol<>,usize)>,
        _: ::std::marker::PhantomData<()>,
    ) -> Option<Result<Program,__lalrpop_util::ParseError<usize, Token, LexError>>>
    {
        let __nonterminal = match -__action {
            1 => {
                // Program =  => ActionFn(7);
                let __start = __symbols.last().map(|s| s.2.clone()).unwrap_or_default();
                let __end = __lookahead_start.cloned().unwrap_or_else(|| __start.clone());
                let __nt = super::__action7::<>(&__start, &__end);
                let __states_len = __states.len();
                __states.truncate(__states_len - 0);
                __symbols.push((__start, __Symbol::NtProgram(__nt), __end));
                0
            }
            2 => {
                // Program = Stmt+ => ActionFn(8);
                let __sym0 = __pop_NtStmt_2b(__symbols);
                let __start = __sym0.0.clone();
                let __end = __sym0.2.clone();
                let __nt = super::__action8::<>(__sym0);
                let __states_len = __states.len();
                __states.truncate(__states_len - 1);
                __symbols.push((__start, __Symbol::NtProgram(__nt), __end));
                0
            }
            3 => {
                // Stmt = ":" => ActionFn(1);
                let __sym0 = __pop_Term_22_3a_22(__symbols);
                let __start = __sym0.0.clone();
                let __end = __sym0.2.clone();
                let __nt = super::__action1::<>(__sym0);
                let __states_len = __states.len();
                __states.truncate(__states_len - 1);
                __symbols.push((__start, __Symbol::NtStmt(__nt), __end));
                1
            }
            4 => {
                // Stmt* =  => ActionFn(3);
                let __start = __symbols.last().map(|s| s.2.clone()).unwrap_or_default();
                let __end = __lookahead_start.cloned().unwrap_or_else(|| __start.clone());
                let __nt = super::__action3::<>(&__start, &__end);
                let __states_len = __states.len();
                __states.truncate(__states_len - 0);
                __symbols.push((__start, __Symbol::NtStmt_2a(__nt), __end));
                2
            }
            5 => {
                // Stmt* = Stmt+ => ActionFn(4);
                let __sym0 = __pop_NtStmt_2b(__symbols);
                let __start = __sym0.0.clone();
                let __end = __sym0.2.clone();
                let __nt = super::__action4::<>(__sym0);
                let __states_len = __states.len();
                __states.truncate(__states_len - 1);
                __symbols.push((__start, __Symbol::NtStmt_2a(__nt), __end));
                2
            }
            6 => {
                // Stmt+ = Stmt => ActionFn(5);
                let __sym0 = __pop_NtStmt(__symbols);
                let __start = __sym0.0.clone();
                let __end = __sym0.2.clone();
                let __nt = super::__action5::<>(__sym0);
                let __states_len = __states.len();
                __states.truncate(__states_len - 1);
                __symbols.push((__start, __Symbol::NtStmt_2b(__nt), __end));
                3
            }
            7 => {
                // Stmt+ = Stmt+, Stmt => ActionFn(6);
                let __sym1 = __pop_NtStmt(__symbols);
                let __sym0 = __pop_NtStmt_2b(__symbols);
                let __start = __sym0.0.clone();
                let __end = __sym1.2.clone();
                let __nt = super::__action6::<>(__sym0, __sym1);
                let __states_len = __states.len();
                __states.truncate(__states_len - 2);
                __symbols.push((__start, __Symbol::NtStmt_2b(__nt), __end));
                3
            }
            8 => {
                // __Program = Program => ActionFn(0);
                let __sym0 = __pop_NtProgram(__symbols);
                let __start = __sym0.0.clone();
                let __end = __sym0.2.clone();
                let __nt = super::__action0::<>(__sym0);
                return Some(Ok(__nt));
            }
            _ => panic!("invalid action code {}", __action)
        };
        let __state = *__states.last().unwrap() as usize;
        let __next_state = __GOTO[__state * 5 + __nonterminal] - 1;
        __states.push(__next_state);
        None
    }
    fn __pop_Term_22_28_22<
    >(
        __symbols: &mut ::std::vec::Vec<(usize,__Symbol<>,usize)>
    ) -> (usize, Token, usize)
     {
        match __symbols.pop().unwrap() {
            (__l, __Symbol::Term_22_28_22(__v), __r) => (__l, __v, __r),
            _ => panic!("symbol type mismatch")
        }
    }
    fn __pop_Term_22_29_22<
    >(
        __symbols: &mut ::std::vec::Vec<(usize,__Symbol<>,usize)>
    ) -> (usize, Token, usize)
     {
        match __symbols.pop().unwrap() {
            (__l, __Symbol::Term_22_29_22(__v), __r) => (__l, __v, __r),
            _ => panic!("symbol type mismatch")
        }
    }
    fn __pop_Term_22_3a_22<
    >(
        __symbols: &mut ::std::vec::Vec<(usize,__Symbol<>,usize)>
    ) -> (usize, Token, usize)
     {
        match __symbols.pop().unwrap() {
            (__l, __Symbol::Term_22_3a_22(__v), __r) => (__l, __v, __r),
            _ => panic!("symbol type mismatch")
        }
    }
    fn __pop_NtProgram<
    >(
        __symbols: &mut ::std::vec::Vec<(usize,__Symbol<>,usize)>
    ) -> (usize, Program, usize)
     {
        match __symbols.pop().unwrap() {
            (__l, __Symbol::NtProgram(__v), __r) => (__l, __v, __r),
            _ => panic!("symbol type mismatch")
        }
    }
    fn __pop_NtStmt<
    >(
        __symbols: &mut ::std::vec::Vec<(usize,__Symbol<>,usize)>
    ) -> (usize, Stmt, usize)
     {
        match __symbols.pop().unwrap() {
            (__l, __Symbol::NtStmt(__v), __r) => (__l, __v, __r),
            _ => panic!("symbol type mismatch")
        }
    }
    fn __pop_NtStmt_2a<
    >(
        __symbols: &mut ::std::vec::Vec<(usize,__Symbol<>,usize)>
    ) -> (usize, ::std::vec::Vec<Stmt>, usize)
     {
        match __symbols.pop().unwrap() {
            (__l, __Symbol::NtStmt_2a(__v), __r) => (__l, __v, __r),
            _ => panic!("symbol type mismatch")
        }
    }
    fn __pop_NtStmt_2b<
    >(
        __symbols: &mut ::std::vec::Vec<(usize,__Symbol<>,usize)>
    ) -> (usize, ::std::vec::Vec<Stmt>, usize)
     {
        match __symbols.pop().unwrap() {
            (__l, __Symbol::NtStmt_2b(__v), __r) => (__l, __v, __r),
            _ => panic!("symbol type mismatch")
        }
    }
    fn __pop_Nt____Program<
    >(
        __symbols: &mut ::std::vec::Vec<(usize,__Symbol<>,usize)>
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
>(
    (_, __0, _): (usize, Program, usize),
) -> Program
{
    (__0)
}

fn __action1<
>(
    (_, __0, _): (usize, Token, usize),
) -> Stmt
{
    Stmt::Expr(Expr::IntLiteral(1))
}

fn __action2<
>(
    (_, __0, _): (usize, ::std::vec::Vec<Stmt>, usize),
) -> Program
{
    Program {}
}

fn __action3<
>(
    __lookbehind: &usize,
    __lookahead: &usize,
) -> ::std::vec::Vec<Stmt>
{
    vec![]
}

fn __action4<
>(
    (_, v, _): (usize, ::std::vec::Vec<Stmt>, usize),
) -> ::std::vec::Vec<Stmt>
{
    v
}

fn __action5<
>(
    (_, __0, _): (usize, Stmt, usize),
) -> ::std::vec::Vec<Stmt>
{
    vec![__0]
}

fn __action6<
>(
    (_, v, _): (usize, ::std::vec::Vec<Stmt>, usize),
    (_, e, _): (usize, Stmt, usize),
) -> ::std::vec::Vec<Stmt>
{
    { let mut v = v; v.push(e); v }
}

fn __action7<
>(
    __lookbehind: &usize,
    __lookahead: &usize,
) -> Program
{
    let __start0 = __lookbehind.clone();
    let __end0 = __lookahead.clone();
    let __temp0 = __action3(
        &__start0,
        &__end0,
    );
    let __temp0 = (__start0, __temp0, __end0);
    __action2(
        __temp0,
    )
}

fn __action8<
>(
    __0: (usize, ::std::vec::Vec<Stmt>, usize),
) -> Program
{
    let __start0 = __0.0.clone();
    let __end0 = __0.2.clone();
    let __temp0 = __action4(
        __0,
    );
    let __temp0 = (__start0, __temp0, __end0);
    __action2(
        __temp0,
    )
}

pub trait __ToTriple<> {
    type Error;
    fn to_triple(value: Self) -> Result<(usize,Token,usize),Self::Error>;
}

impl<> __ToTriple<> for (usize, Token, usize) {
    type Error = LexError;
    fn to_triple(value: Self) -> Result<(usize,Token,usize),LexError> {
        Ok(value)
    }
}
impl<> __ToTriple<> for Result<(usize, Token, usize),LexError> {
    type Error = LexError;
    fn to_triple(value: Self) -> Result<(usize,Token,usize),LexError> {
        value
    }
}
