#include <boost/program_options.hpp>

#include <llvm/Support/Host.h>
#include <llvm/Support/TargetRegistry.h>
#include <llvm/Support/TargetSelect.h>
#include <llvm/Target/TargetMachine.h>
#include <llvm/Target/TargetOptions.h>

#include <fstream>
#include <iostream>

#include "ast.hh"
#include "context.hh"
#include "driver.hh"
#include "exceptions.hh"

int compiler_main(int argc, char **argv) {
    typhon::Context ctx;
    typhon::Driver driver(ctx);

    bool optc = false;

    namespace po = boost::program_options;
    po::options_description desc("Compiler");
    desc.add_options()(",c", "Emit object file instead of binary.")("help,h", "Display help message.")("file", po::value<std::string>(),
                                                                                                       "File to compile.");

    po::positional_options_description pos;
    pos.add("file", 1);

    // if (argc < 2) {
    //     std::cerr << "please provide a file to compile" << std::endl;
    //     return 1;
    // }
    po::variables_map vm;
    try {
        po::store(po::command_line_parser(argc, argv).options(desc).positional(pos).run(), vm);
        po::notify(vm);
        // for (auto it = vm.begin(); it != vm.end(); ++it) {
        //     std::cout << it->first << ": " << it->second.as<std::string>() << std::endl;
        // }
        if (vm.count("help")) {
            std::cout << desc << std::endl;
            return 0;
        }
        if (vm.count("-c"))
            optc = true;
    } catch (std::exception &e) {
        std::cerr << "Unhandled Exception: " << e.what() << ". application will now exit" << std::endl;
        return 1;
    }

    if (!vm.count("file")) {
        std::cerr << "please provide a file to compile" << std::endl;
        return 1;
    }
    // std::cout << "filename: " << vm["file"].as<std::string>() << std::endl;
    // std::cout << optc << std::endl;

    std::ifstream ifile(vm["file"].as<std::string>());
    if (!ifile.is_open()) {
        std::cerr << "unable to open file" << std::endl;
        return 1;
    }

    if (driver.parse_stream(ifile)) {
        ifile.close(); // close the file first
        typhon::ast::Block *block = driver.block;
        typhon::mir::Node *root = block->convert();

        // ok start llvm shit
        auto TargetTriple = llvm::sys::getDefaultTargetTriple();
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
