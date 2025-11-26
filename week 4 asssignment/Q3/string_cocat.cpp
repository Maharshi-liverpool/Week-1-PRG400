#include <pybind11/pybind11.h>
#include <string>

namespace py = pybind11;

std::string concat_strings(std::string a, std::string b) {
return a + b;
}

PYBIND11_MODULE(string_concat, m) {
m.def("concat", &concat_strings, "Concatenate two strings");
}