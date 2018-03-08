#include <iostream>

#include "context.hh"
#include "driver.hh"

int main() {
    typhon::Context ctx;
    typhon::Driver driver(ctx);

    // main loop
    std::string line;
    while (std::cout << "tp> " && std::getline(std::cin, line) &&
           !std::cin.eof()) {
        driver.parse_string(line, "input");
    }
}
