package main

import (
	"fmt"
	"math/rand"
	"time"
)

func generateRandomMatrix(rows, cols int) [][]int {
	matrix := make([][]int, rows)
	for i := range matrix {
		matrix[i] = make([]int, cols)
		for j := range matrix[i] {
			matrix[i][j] = rand.Intn(10)
		}
	}
	return matrix
}

func mul(mat1 [][]int, mat2 [][]int) [][]int {
	rows1, cols1 := len(mat1), len(mat1[0])
	rows2, cols2 := len(mat2), len(mat2[0])

	if cols1 != rows2 {
		return nil // dimension mismatch
	}

	result := make([][]int, rows1)
	for i := range result {
		result[i] = make([]int, cols2)
	}

	for i := 0; i < rows1; i++ {
		for j := 0; j < cols2; j++ {
			for k := 0; k < cols1; k++ {
				result[i][j] += mat1[i][k] * mat2[k][j]
			}
		}
	}

	return result
}

func main() {
	const size = 1000
	rand.Seed(time.Now().UnixNano())

	mat1 := generateRandomMatrix(size, size)
	mat2 := generateRandomMatrix(size, size)

	start := time.Now()
	result := mul(mat1, mat2)
	elapsed := time.Since(start)

	if result == nil {
		fmt.Println("Matrix multiplication failed (dimension mismatch).")
		return
	}

	fmt.Printf("%.2fs\n", elapsed.Seconds())
}

