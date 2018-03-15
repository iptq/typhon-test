#include "types.hh"

namespace typhon {
namespace type {

Type::Type(std::string _name) { name = _name; }

std::string Type::to_string() { return name; }

} // namespace type
} // namespace typhon
