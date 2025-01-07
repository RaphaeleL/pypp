import ccms_ccore_matrix
import random, time

# Generate NxN matrices with random integers
size = 1_000
mat1 = [[random.randint(1, 10) for _ in range(size)] for _ in range(size)]
mat2 = [[random.randint(1, 10) for _ in range(size)] for _ in range(size)]

# Measure execution time
start_time = time.time()

# Perform matrix multiplication
_ = ccms_ccore_matrix.mul(mat1, mat2)

# Time taken
end_time = time.time()
print(f"{round(end_time - start_time, 2)}s")
