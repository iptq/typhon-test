#ifndef SRC_DRIVER_H_
#define SRC_DRIVER_H_

#include <string>
#include <vector>

class CalcContext;

namespace typhon {

class Driver
{
public:
    Driver(class CalcContext& calc);
    bool trace_scanning;
    bool trace_parsing;
    std::string streamname;

    bool parse_stream(std::istream& in,const std::string& sname = "stream input");
    bool parse_string(const std::string& input, const std::string& sname = "string stream");
    bool parse_file(const std::string& filename);
    void error(const class location& l, const std::string& m);
    void error(const std::string& m);

    class Scanner* lexer;
    class CalcContext& calc;
};

} // namespace typhon

#endif
