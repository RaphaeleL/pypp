import random
import time

def matrix_multiply(mat1, mat2):
    rows1 = len(mat1)
    cols1 = len(mat1[0])
    rows2 = len(mat2)
    cols2 = len(mat2[0])

    if cols1 != rows2:
        raise ValueError("Incompatible matrix dimensions for multiplication.")

    # Initialize the result matrix with zeros
    result = [[0] * cols2 for _ in range(rows1)]

    # Perform matrix multiplication
    for i in range(rows1):
        for j in range(cols2):
            for k in range(cols1):
                result[i][j] += mat1[i][k] * mat2[k][j]

    return result

# Generate NxN matrices with random integers
size = 1_000
mat1 = [[random.randint(1, 10) for _ in range(size)] for _ in range(size)]
mat2 = [[random.randint(1, 10) for _ in range(size)] for _ in range(size)]

# Measure execution time
start_time = time.time()

# Perform matrix multiplication
_ = matrix_multiply(mat1, mat2)

# Time taken
end_time = time.time()
print(f"{round(end_time - start_time, 2)}s")
