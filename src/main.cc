#include <fstream>
#include <iostream>

#include "ast.hh"
#include "context.hh"
#include "driver.hh"
#include "exceptions.hh"

int compiler_main(int argc, char **argv) {
    typhon::Context ctx;
    typhon::Driver driver(ctx);

    if (argc < 2) {
        std::cerr << "please provide a file to compile" << std::endl;
        return 1;
    }

    std::ifstream ifile(argv[1]);
    if (!ifile.is_open()) {
        std::cerr << "unable to open file" << std::endl;
        return 1;
    }

    if (driver.parse_stream(ifile)) {
        ifile.close(); // close the file first
        typhon::ast::Block *block = driver.block;
        typhon::mir::Node *root = block->convert();
    }
    return 0;
}

int interpreter_main() {
    typhon::Context ctx;
    typhon::Driver driver(ctx);

    // main loop
    std::string line;
    while (std::cout << "tp> " and std::getline(std::cin, line) and !std::cin.eof()) {
        try {
            driver.parse_string(line, "input");
        } catch (typhon::ParseError e) {
            std::cout << "[!] ParseError: TODO" << std::endl;
        } catch (typhon::TypeError e) {
            std::cout << "[!] TypeError: TODO" << std::endl;
        } catch (typhon::UnboundVariableError e) {
            std::cout << "[!] UnboundVariableError: TODO" << std::endl;
        }
    }
    return 0;
}

int main(int argc, char **argv) {
#ifdef COMPILER
    return compiler_main(argc, argv);
#else
#ifdef INTERPRETER
    return interpreter_main();
#endif
#endif
}
