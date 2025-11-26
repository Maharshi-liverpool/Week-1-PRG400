from setuptools import setup, Extension
import pybind11

# Get pybind11 include path
include_path = pybind11.get_include()

# Define the extension module
string_concat_module = Extension(
    "string_concat",
    sources=["string_concat.cpp"],
    include_dirs=[include_path],
    language="c++",
    extra_compile_args=["-std=c++11"],
)

setup(
    name="string_concat",
    version="1.0",
    description="Pybind11 string concatenation module",
    ext_modules=[string_concat_module],
)