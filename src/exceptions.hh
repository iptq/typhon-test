#ifndef SRC_EXCEPTIONS_H_
#define SRC_EXCEPTIONS_H_

#include <exception>

namespace typhon {

struct UnboundVariableException : public std::exception {};

} // namespace typhon

#endif