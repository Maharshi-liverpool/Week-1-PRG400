from setuptools import setup, Extension

module = Extension("array_manager", sources=["array_manager_module.c"])

setup(
name="array_manager",
version="1.0",
ext_modules=[module]
)