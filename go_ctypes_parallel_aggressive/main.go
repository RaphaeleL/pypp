package main

/*
#include <stdlib.h>
*/
import "C"

import (
	"runtime"
	"sync"
	"unsafe"
)

const blockSize = 32 // Can tune based on L1/L2 cache

// job for a block
type blockJob struct {
	rowBlock, colBlock int
}

//export mul
func mul(mat1 *C.int, rows1, cols1 C.int, mat2 *C.int, rows2, cols2 C.int) *C.int {
	if cols1 != rows2 {
		return nil
	}

	totalRows1 := int(rows1)
	totalCols1 := int(cols1)
	totalCols2 := int(cols2)

	result := C.malloc(C.size_t(rows1*cols2) * C.size_t(C.sizeof_int))
	if result == nil {
		return nil
	}

	res := (*[1 << 30]C.int)(result)[: totalRows1*totalCols2 : totalRows1*totalCols2]
	m1 := (*[1 << 30]C.int)(unsafe.Pointer(mat1))[: totalRows1*totalCols1 : totalRows1*totalCols1]
	m2 := (*[1 << 30]C.int)(unsafe.Pointer(mat2))[: int(rows2)*totalCols2 : int(rows2)*totalCols2]

	numWorkers := runtime.NumCPU()
	jobChan := make(chan blockJob, numWorkers*2)
	var wg sync.WaitGroup

	// Workers
	for w := 0; w < numWorkers; w++ {
		wg.Add(1)
		go func() {
			defer wg.Done()
			for job := range jobChan {
				rowStart := job.rowBlock * blockSize
				colStart := job.colBlock * blockSize
				rowEnd := min(rowStart+blockSize, totalRows1)
				colEnd := min(colStart+blockSize, totalCols2)

				for i := rowStart; i < rowEnd; i++ {
					for j := colStart; j < colEnd; j++ {
						sum := C.int(0)
						for k := 0; k < totalCols1; k++ {
							sum += m1[i*totalCols1+k] * m2[k*totalCols2+j]
						}
						res[i*totalCols2+j] = sum
					}
				}
			}
		}()
	}

	// Enqueue block jobs
	for i := 0; i < (totalRows1+blockSize-1)/blockSize; i++ {
		for j := 0; j < (totalCols2+blockSize-1)/blockSize; j++ {
			jobChan <- blockJob{rowBlock: i, colBlock: j}
		}
	}
	close(jobChan)

	wg.Wait()
	return (*C.int)(result)
}

//export free_matrix
func free_matrix(ptr *C.int) {
	C.free(unsafe.Pointer(ptr))
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func main() {}
