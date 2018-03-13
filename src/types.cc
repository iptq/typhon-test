#include <string>

#include "types.hh"

namespace typhon {
namespace type {

type::TypeOperator Prim_Int32("int");

TypeOperator::TypeOperator(std::string _name) { name = _name; }

} // namespace type
} // namespace typhon
