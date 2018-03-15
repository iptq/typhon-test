#include <iostream>

#include "context.hh"
#include "driver.hh"
#include "exceptions.hh"

int main() {
#ifdef INTERPRETER
    typhon::Context ctx;
    typhon::Driver driver(ctx);

    // main loop
    std::string line;
    while (std::cout << "tp> " && std::getline(std::cin, line) && !std::cin.eof()) {
        try {
            driver.parse_string(line, "input");
        } catch (typhon::TypeError e) {
            std::cout << "[!] TypeError: TODO" << std::endl;
        } catch (typhon::UnboundVariableError e) {
            std::cout << "[!] UnboundVariableError: TODO" << std::endl;
        }
    }
#endif
}
