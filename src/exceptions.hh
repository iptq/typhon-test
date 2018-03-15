#ifndef SRC_EXCEPTIONS_H_
#define SRC_EXCEPTIONS_H_

#include <exception>

namespace typhon {

struct UnboundVariableError : public std::exception {};

struct TypeError : public std::exception {};

} // namespace typhon

#endif