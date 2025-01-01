# CPY

This project demonstrates the performance comparison of matrix multiplication implementations using Python and C. It includes three variations:

1. **Pure Python Implementation** (`plain.py`).
2. **C-based Implementation with `ctypes`** (`v1`) in Python.
3. **C Extension Module for Python** (`v2`) in Python.

## Overview

Matrix multiplication is a fundamental operation in many computational fields, and optimizing its performance can lead to significant improvements in computational-heavy applications. In this project, we compare the time it takes for matrix multiplication using pure Python, C with `ctypes`, and C as a Python extension module.

## Directory Structure

```
.
├── README.md             # This file
├── plain.py              # Python-only matrix multiplication
├── v1                    # C-based solution using ctypes
│   ├── Makefile          # Build instructions for v1
│   ├── lib_matrix_mul.so # Compiled C shared library
│   ├── main.py           # Python script using C with ctypes
│   └── matrix_mul.c      # C code for matrix multiplication
└── v2                    # Python C extension module
    ├── Makefile          # Build instructions for v2
    ├── build             # Build artifacts
    ├── main.py           # Python script using the extension module
    ├── matrix_mul.c      # C code for matrix multiplication
    ├── matrix_mul.cpython-313-darwin.so  # Compiled extension module
    └── setup.py          # Setup script for building v2 extension
```

## Implementations

### 1. **Pure Python Implementation** (`plain.py`)

This implementation uses Python lists and loops to perform matrix multiplication. While it is easy to understand and works well for small matrices, it is significantly slower for larger matrices due to the inefficiencies of interpreted code.

### 2. **C-based Implementation using `ctypes`** (`v1`)

The `v1` implementation uses C code for matrix multiplication, and Python interacts with the C library using `ctypes`. This method is faster than the pure Python version, as C code is compiled and optimized for speed.

- **C Code** (`matrix_mul.c`): Contains the C function for matrix multiplication.
- **Python Code** (`main.py`): Uses `ctypes` to load and call the C function.

### 3. **Python C Extension Module** (`v2`)

The `v2` implementation exposes the C matrix multiplication function as a Python extension module, making it easier to call from Python directly. This method is the most integrated and optimal, as it combines the efficiency of C with the flexibility of Python.

- **C Code** (`matrix_mul.c`): Implements the matrix multiplication function.
- **Python Code** (`main.py`): Imports the C extension module and uses it to perform the multiplication.
- **Setup** (`setup.py`): For building the Python extension.

## Performance Comparison

For a 100x100 matrix multiplication, the performance results are as follows:

| Implementation                       | Time Taken       |
|--------------------------------------|------------------|
| **Python-only (plain.py)**           | 62.894 seconds   |
| **C-based (`ctypes`, v1)**           | 2.5070 seconds   |
| **C Extension Module (v2)**          | 7.6621 seconds   |

As seen, the C-based implementations (either with `ctypes` or as a Python extension module) are **significantly faster** than the pure Python solution.

## How to Run

### 1. **Pure Python Implementation**

To run the Python-only version, simply execute:

```bash
python3 plain.py
```

### 2. **C-based Implementation (`v1`)**

To build and run the `v1` version using `ctypes`:

```bash
# Build the C shared library
make -C v1 create 

# Run the Python script using ctypes
make -C v1 run 

# NOTE: Alternative -> Compare Plain with v1 directly 
make -C v1 compare 
```

### 3. **Python C Extension Module (`v2`)**

To build and run the Python C extension module:

```bash
# Build the C extension module
make -C v2 create 

# Run the Python script using the C extension
make -C v2 run 

# NOTE: Alternative -> Compare Plain with v2 directly 
make -C v2 compare 
```

