# Python3 in Fast 

This project demonstrates the performance comparison of matrix multiplication implementations using Python3 with different Backends.

## How to Run

> **Note:** Install all compilers and interpreters before running the benchmarks.

Simply use `make benchmark`. To run the benchmark on a specific implementation, just run the `make` command with the desired implementation folder. For example, to run the benchmark for the `C` implementation, use: `make c`

## Performance Comparison

For a 1000x1000 matrix multiplication, the performance results are as follows:

| Implementation                                                                        | Time Taken (Intel(R) Xeon(R) Gold 6348 (4) @ 2.60 GHz)  | Time Taken (M1 Pro 16 GB) |
|---------------------------------------------------------------------------------------|---------------------------------------------------------|---------------------------|
| **C**                                                                                 | 4.32 sec                                                | 2.19 sec                  |
| **Go**                                                                                | 3.67 sec                                                | 3.42 sec                  |
| **Python3**                                                                           | **104.67 sec**                                          | 61.29 sec                 |
| **Python3 with C Backend** through Shared Libs and Ctypes                             | 5.46 sec                                                | 2.43 sec                  |
| **Python3 with C Backend** through Shared Libs and the 'Python.h' Headerfile          | 18.51 sec                                               | 8.48 sec                  |
| **Python3 with Go Backend** through Shared Libs and Ctypes                            | 2.84 sec                                                | 1.15 sec                  |
| **Python3 with Go Backend** through Shared Libs and Ctypes in Parallel                | **n/a**                                                 | **0.14 sec**              |
| **Python3 with Go Backend** through Shared Libs and Ctypes in aggressive Parallelism  | **n/a**                                                 | **0.12 sec**              |

The performance results may vary based on the system you are using and do not include the time taken to compile the C and Go implementations. In addition, there was no parallelism tricks used in Go. The Implementation of the Matrix multiplication is the same in each Language / Backend.

## Result 

> Literally, everthing is better then Python3! Somehow Python3 with the Go Background through Shared and CTypes is the fastest!

The results show that using a backend like Go or C can significantly improve the performance of Python3. The native Python3 implementation is the slowest, while using Go or C as a backend can lead to substantial performance gains. 

If we use Parallelism in Go, we can notice an even bigger performance gain.
