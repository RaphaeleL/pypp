create:
	python3 setup.py build_ext --inplace

run:
	python3 main.py

clean:
	rm -rf build module_matrix_mul.cpython-313-darwin.so

compare: 
	python3 main.py
	python3 ../plain.py
