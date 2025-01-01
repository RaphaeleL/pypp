import matrix_mul
import random, time

# Generate 100x100 matrices with random integers
size = 1_000
mat1 = [[random.randint(1, 10) for _ in range(size)] for _ in range(size)]
mat2 = [[random.randint(1, 10) for _ in range(size)] for _ in range(size)]

# Measure execution time
start_time = time.time()

# Perform matrix multiplication
_ = matrix_mul.matrix_mul(mat1, mat2)

# Time taken
end_time = time.time()
print(f"Time taken for {size}x{size} matrix multiplication in C: {end_time - start_time} seconds")
