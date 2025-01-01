import ctypes
import random, time

# Load the shared library
lib = ctypes.CDLL('./matrix_mul.so')

# Specify argument and return types for the matrix_mul function
lib.matrix_mul.argtypes = (
    ctypes.POINTER(ctypes.c_int), # mat1
    ctypes.c_int,                 # rows1
    ctypes.c_int,                 # cols1
    ctypes.POINTER(ctypes.c_int), # mat2
    ctypes.c_int,                 # rows2
    ctypes.c_int,                 # cols2
)
lib.matrix_mul.restype = ctypes.POINTER(ctypes.c_int)  # Returns pointer to int array

# Specify argument for the free_matrix function
lib.free_matrix.argtypes = (ctypes.POINTER(ctypes.c_int),)

# Generate NxN matrices with random integers
size = 1_000
mat1 = [[random.randint(1, 10) for _ in range(size)] for _ in range(size)]
mat2 = [[random.randint(1, 10) for _ in range(size)] for _ in range(size)]

# Measure execution time
start_time = time.time()

# Flatten the matrices into 1D arrays
rows1, cols1 = len(mat1), len(mat1[0])
rows2, cols2 = len(mat2), len(mat2[0])
flat_mat1 = [item for row in mat1 for item in row]
flat_mat2 = [item for row in mat2 for item in row]

# Convert the matrices to ctypes arrays
array1 = (ctypes.c_int * len(flat_mat1))(*flat_mat1)
array2 = (ctypes.c_int * len(flat_mat2))(*flat_mat2)

# Call the matrix_mul function
result_ptr = lib.matrix_mul(array1, rows1, cols1, array2, rows2, cols2)
if not result_ptr:
    raise ValueError("Matrix multiplication failed due to dimension mismatch.")

# Convert the result back to a Python 2D list
result = [
    [result_ptr[i * cols2 + j] for j in range(cols2)]
    for i in range(rows1)
]

# Free the allocated memory in C
lib.free_matrix(result_ptr)

# Time taken
end_time = time.time()
print(f"Time taken for {size}x{size} matrix multiplication in C: {end_time - start_time} seconds")
