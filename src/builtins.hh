#ifndef SRC_BUILTINS_H_
#define SRC_BUILTINS_H_

#include "types.hh"

namespace typhon {

extern type::PrimitiveType Prim_Char;
extern type::PrimitiveType Prim_Int32;

class StringType : public type::Type {};

}; // namespace typhon

#endif