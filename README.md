# CPY

This project demonstrates the performance comparison of matrix multiplication implementations using Python and C. It includes several variations.

## How to Run

> If you want to compare all, simply use `run.sh`

- Run a 100% C Version: `make -C basic_c -B`
- Run a 100% Python Version: `make -C basic_py -B`
- Run C in Python3 with Shared Libs and Ctypes for the Datatypes: `make -C ctypes -B`
- Run C in Python3 with Shared Libs and the 'Python.h' Header for the Datatypes: `make -C py_header -B`

## Performance Comparison

For a 1000x1000 matrix multiplication, the performance results are as follows (MacBook Pro, M1 Pro, 16 GB):

| Implementation                                                                    | Time Taken (M1 Pro, 16 GB) | Time Taken (Linux, 16 GB) |
|-----------------------------------------------------------------------------------|----------------------------|---------------------------|
| **100% C**                                                                        | 2.08 sec                   | 4.59 sec                  |
| **C in Python3** with Shared Libs and **Ctypes for the Datatypes**                | 2.33 sec                   | 5.21 sec                  |
| **C in Python3** with Shared Libs and **the 'Python.h' Header for the Datatypes** | 8.36 sec                   | 16.71 sec                 |
| **100% Python3**                                                                  | 61.21 sec                  | 149.31 sec                |

## Result

As seen, the C-based implementations (either with `ctypes` or with the `Python.h` Header) are **significantly faster** than the pure Python solution.
