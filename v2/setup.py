from setuptools import setup, Extension

module = Extension(
    "matrix_mul",  # Module name
    sources=["matrix_mul.c"],  # C source file
)

setup(
    name="matrix_mul",
    version="1.0",
    description="Matrix multiplication using C",
    ext_modules=[module],
)

