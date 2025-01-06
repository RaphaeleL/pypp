# CPY

This project demonstrates the performance comparison of matrix multiplication implementations using Python and C. It includes several variations.

## How to Run

- Run a 100% Python Version: `make -C basic_py -B`
- Run C in Python3 with Shared Libs and Ctypes for the Datatypes: `make -C ctypes -B`
- Run C in Python3 with Shared Libs and the 'Python.h' Header for the Datatypes: `make -C py_header -B`

## Performance Comparison

For a 1000x1000 matrix multiplication, the performance results are as follows (MacBook Pro, M1 Pro, 16 GB):

| Implementation                                                                    | Time Taken |
|-----------------------------------------------------------------------------------|------------|
| **C in Python3** with Shared Libs and **Ctypes for the Datatypes**                | 02.33 sec  |
| **C in Python3** with Shared Libs and **the 'Python.h' Header for the Datatypes** | 08.36 sec  |
| **100% Python3**                                                                  | 61.21 sec  |

## Result

As seen, the C-based implementations (either with `ctypes` or with the `Python.h` Header) are **significantly faster** than the pure Python solution.
