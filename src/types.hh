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
    std::string name;
};

} // namespace type
} // namespace typhon

#endif
