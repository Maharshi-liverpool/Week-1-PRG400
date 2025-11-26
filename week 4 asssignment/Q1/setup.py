from setuptools import setup, Extension

module = Extension("squaremodule", sources=["squaremodule.c"])

setup(
name="squaremodule",
version="1.0",
ext_modules=[module]
)