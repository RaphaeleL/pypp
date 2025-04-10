# Python3 in Fast 

This project demonstrates the performance comparison of matrix multiplication implementations using Python3 with different Backends.

## How to Run

> **Note:** Install all compilers and interpreters before running the benchmarks.

Simply use `make benchmark`. To run the benchmark on a specific implementation, just run the `make` command with the desired implementation folder. For example, to run the benchmark for the `C` implementation, use: `cd c; make`

## Performance Comparison

For a 1000x1000 matrix multiplication, the performance results are as follows:

| Implementation                                                                    | Time Taken                |
|-----------------------------------------------------------------------------------|---------------------------|
| **Python3 with Go Backend** through Shared Libs and Ctypes                        | 3.01 sec                  |
| **Go**                                                                            | 3.67 sec                  |
| **C**                                                                             | 4.32 sec                  |
| **Python3 with C Backend** through Shared Libs and Ctypes                         | 5.46 sec                  |
| **Python3 with C Backend** through Shared Libs and the 'Python.h' Headerfile      | 18.71 sec                 |
| **Python3**                                                                       | **101.61 sec**            |

The performance results may vary based on the system you are using and do not include the time taken to compile the C and Go implementations. In addition, there was no parallelism tricks used in Go. The Implementation of the Matrix multiplication is the same in each Language / Backend.

## Result 

> Literally, everthing is better then Python3!

The results show that using a backend like Go or C can significantly improve the performance of Python3. The native Python3 implementation is the slowest, while using Go or C as a backend can lead to substantial performance gains.
