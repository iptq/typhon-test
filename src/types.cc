#include <iostream>

#include "types.hh"

namespace typhon {
namespace type {

Type::Type(std::string _name) { name = _name; }

bool Type::operator==(const Type *other) {
    std::cout << "SHIET" << std::endl;
    if (dynamic_cast<PrimitiveType *>(this) and dynamic_cast<const PrimitiveType *>(other))
        return name == other->name;
    return false;
}

std::string Type::to_string() { return name; }

} // namespace type
} // namespace typhon
