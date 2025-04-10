.PHONY: benchmark

benchmark: 
	@echo "Time taken for 1000x1000 matrix multiplication in:"

	@echo -n '- C ....................................... '
	@$(MAKE) -C c -B --no-print-directory

	@echo -n '- Go ...................................... '
	@$(MAKE) -C go -B --no-print-directory

	@echo -n '- Python3 ................................. '
	@$(MAKE) -C py -B --no-print-directory

	@echo -n '- Python3 with C Backend through ctypes ... '
	@$(MAKE) -C c_ctypes -B --no-print-directory

	@echo -n '- Python3 with C Backend through Python.h . '
	@$(MAKE) -C c_pyheader -B --no-print-directory

	@echo -n '- Python3 with Go Backend through ctypes .. '
	@$(MAKE) -C go_ctypes -B --no-print-directory

