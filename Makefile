.PHONY: benchmark c go py c_ctypes c_pyheader go_ctypes go_ctypes_parallel go_ctypes_parallel_aggressive

c: 
	@echo -n '- C ................................................................. '
	@$(MAKE) -C src/go -B --no-print-directory

go: 
	@echo -n '- Go ................................................................ '
	@$(MAKE) -C src/go -B --no-print-directory

py:
	@echo -n '- Python3 ........................................................... '
	@$(MAKE) -C src/py -B --no-print-directory

c_ctypes:
	@echo -n '- Python3 with C Backend through ctypes ............................. '
	@$(MAKE) -C src/c_ctypes -B --no-print-directory

c_pyheader:
	@echo -n '- Python3 with C Backend through Python.h ........................... '
	@$(MAKE) -C src/c_pyheader -B --no-print-directory

go_ctypes:
	@echo -n '- Python3 with Go Backend through ctypes ............................ '
	@$(MAKE) -C src/go_ctypes -B --no-print-directory

go_ctypes_parallel:
	@echo -n '- Python3 with Go Backend through ctypes in Parallel ................ '
	@$(MAKE) -C src/go_ctypes_parallel -B --no-print-directory

go_ctypes_parallel_aggressive:
	@echo -n '- Python3 with Go Backend through ctypes in aggressive Parallelism .. '
	@$(MAKE) -C src/go_ctypes_parallel_aggressive -B --no-print-directory

benchmark:
	@echo "Time taken for 1000x1000 matrix multiplication in:"
	@$(MAKE) c -B --no-print-directory
	@$(MAKE) go -B --no-print-directory
	@$(MAKE) py -B --no-print-directory
	@$(MAKE) c_ctypes -B --no-print-directory
	@$(MAKE) c_pyheader -B --no-print-directory
	@$(MAKE) go_ctypes -B --no-print-directory
	@$(MAKE) go_ctypes_parallel -B --no-print-directory
	@$(MAKE) go_ctypes_parallel_aggressive -B --no-print-directory

