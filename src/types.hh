#ifndef SRC_TYPES_H_
#define SRC_TYPES_H_

namespace typhon {
namespace type {

class Type {};

enum PRIMITIVES { TYPE_INT32, TYPE_UINT32, TYPE_CHAR, TYPE_BOOL };

class PrimitiveType : public Type {
  public:
    PrimitiveType(enum PRIMITIVES _name) : name(_name) {}
    enum PRIMITIVES name;
};

} // namespace type
} // namespace typhon

#endif