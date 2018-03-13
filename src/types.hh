#ifndef SRC_TYPES_H_
#define SRC_TYPES_H_

namespace typhon {
namespace type {

class TypeOperator;
extern TypeOperator Prim_Int32;

// used for unknown types
class TypeVariable {};

// combine multiple tyeps
class TypeOperator {
  public:
    TypeOperator(std::string name);
    std::string name;
};

} // namespace type
} // namespace typhon

#endif
