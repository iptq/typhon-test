#ifndef SRC_MIR_H_
#define SRC_MIR_H_

#include <llvm/IR/Value.h>

namespace typhon {
namespace mir {

class Node {
  public:
    virtual llvm::Value *codegen() {}
};

class Constant : public Node {
  public:
};

} // namespace mir
} // namespace typhon

#endif