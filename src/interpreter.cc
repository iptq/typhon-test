#include <iostream>

#include "context.hh"
#include "driver.hh"
#include "exceptions.hh"

int main() {
    typhon::Context ctx;
    typhon::Driver driver(ctx);

    // main loop
    std::string line;
    while (std::cout << "tp> " && std::getline(std::cin, line) && !std::cin.eof()) {
        try {
            driver.parse_string(line, "input");
        } catch (typhon::UnboundVariableException e) {
            std::cout << "[!] Error: Unbound variable." << std::endl;
        }
    }
}
