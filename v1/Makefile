create: 
	gcc -shared -o lib_matrix_mul.so -fPIC matrix_mul.c

run:
	python3 main.py

compare: 
	python3 main.py
	python3 ../plain.py
