# Python3 in Fast 

This project demonstrates the performance comparison of matrix multiplication implementations using Python3 with different Backends.

## How to Run

> **Note:** Install all compilers and interpreters before running the benchmarks

Simply use `make benchmark`. To run the benchmark on a specific implementation, just run the `make` command with the desired implementation folder. For example, to run the benchmark for the `C` implementation, use: `cd c; make`

## Performance Comparison

> **Note:** The performance results may vary based on the system you are using. 

For a 1000x1000 matrix multiplication, the performance results are as follows:

| Implementation                                                                    | Time Taken (Linux, 16 GB) |
|-----------------------------------------------------------------------------------|---------------------------|
| **Python3 with Go Backend** through Shared Libs and Ctypes                        | 3.01 sec                  |
| **Go**                                                                            | 3.67 sec                  |
| **C**                                                                             | 4.32 sec                  |
| **Python3 with C Backend** through Shared Libs and Ctypes                         | 5.46 sec                  |
| **Python3 with C Backend** through Shared Libs and the 'Python.h' Headerfile      | 18.71 sec                 |
| **Python3**                                                                       | 101.61 sec                |
