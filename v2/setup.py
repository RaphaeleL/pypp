from setuptools import setup, Extension

module = Extension(
    "matrix_mul_v2",  # Module name
    sources=["matrix_mul_v2.c"],  # C source file
)

setup(
    name="matrix_mul_v2",
    version="1.0",
    description="Matrix multiplication using C",
    ext_modules=[module],
)

