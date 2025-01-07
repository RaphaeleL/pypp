#!/bin/sh

echo "Time taken for 1000x1000 matrix multiplication in:"

echo -n '- C                 '
make -C basic_c -B --no-print-directory

echo -n '- C with ctypes     '
make -C ctypes -B --no-print-directory

echo -n '- C with Python.h   '
make -C py_header -B --no-print-directory

echo -n '- Python3           '
make -C basic_py -B --no-print-directory
