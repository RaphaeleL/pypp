import ctypes
import random
import time

# Load Go shared library
lib = ctypes.CDLL('./main.so')

# Function prototypes
lib.mul.argtypes = (
    ctypes.POINTER(ctypes.c_int),
    ctypes.c_int,
    ctypes.c_int,
    ctypes.POINTER(ctypes.c_int),
    ctypes.c_int,
    ctypes.c_int,
)
lib.mul.restype = ctypes.POINTER(ctypes.c_int)

lib.free_matrix.argtypes = (ctypes.POINTER(ctypes.c_int),)

# Generate matrices
size = 1000
mat1 = [[random.randint(0, 9) for _ in range(size)] for _ in range(size)]
mat2 = [[random.randint(0, 9) for _ in range(size)] for _ in range(size)]

flat1 = [x for row in mat1 for x in row]
flat2 = [x for row in mat2 for x in row]

array1 = (ctypes.c_int * len(flat1))(*flat1)
array2 = (ctypes.c_int * len(flat2))(*flat2)

start = time.time()

result_ptr = lib.mul(array1, size, size, array2, size, size)

if not result_ptr:
    raise ValueError("Matrix multiplication failed (dim mismatch or malloc failed)")

lib.free_matrix(result_ptr)

end = time.time()
print(f"{round(end - start, 2)}s")

