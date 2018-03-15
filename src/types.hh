#ifndef SRC_TYPES_H_
#define SRC_TYPES_H_

#include <string>

namespace typhon {
namespace type {

// used for unknown types
class TypeVariable {};

// combine multiple tyeps
class Type {
  public:
    Type(std::string name);
    bool operator==(const Type *other);
    bool operator!=(const Type *other) { return operator==(other); }
    virtual std::string to_string();
    std::string name;
};

class PrimitiveType : public Type {
  public:
    PrimitiveType(std::string name) : Type(name){};
};

} // namespace type
} // namespace typhon

#endif
