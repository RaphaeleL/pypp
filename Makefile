.PHONY: benchmark c go py c_ctypes c_pyheader go_ctypes go_ctypes_parallel go_ctypes_parallel_aggressive

c: 
	@echo -n '- C ................................................................. '
	@$(MAKE) -C go -B --no-print-directory

go: 
	@echo -n '- Go ................................................................ '
	@$(MAKE) -C go -B --no-print-directory

py:
	@echo -n '- Python3 ........................................................... '
	@$(MAKE) -C py -B --no-print-directory

c_ctypes:
	@echo -n '- Python3 with C Backend through ctypes ............................. '
	@$(MAKE) -C c_ctypes -B --no-print-directory

c_pyheader:
	@echo -n '- Python3 with C Backend through Python.h ........................... '
	@$(MAKE) -C c_pyheader -B --no-print-directory

go_ctypes:
	@echo -n '- Python3 with Go Backend through ctypes ............................ '
	@$(MAKE) -C go_ctypes -B --no-print-directory

go_ctypes_parallel:
	@echo -n '- Python3 with Go Backend through ctypes in Parallel ................ '
	@$(MAKE) -C go_ctypes_parallel -B --no-print-directory

go_ctypes_parallel_aggressive:
	@echo -n '- Python3 with Go Backend through ctypes in aggressive Parallelism ... '
	@$(MAKE) -C go_ctypes_parallel_aggressive -B --no-print-directory

benchmark:
	@echo "Time taken for 1000x1000 matrix multiplication in:"
	@$(MAKE) c
	@$(MAKE) go
	@$(MAKE) py
	@$(MAKE) c_ctypes
	@$(MAKE) c_pyheader
	@$(MAKE) go_ctypes
	@$(MAKE) go_ctypes_parallel
	@$(MAKE) go_ctypes_parallelgo_ctypes_parallel_aggressive

