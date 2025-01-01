.PHONY: v0 v1 v2 v3

v0: 
	@python3 plain.py

v1: 
	@make -C v1

v2: 
	@make -C v2

v3: 
	@make -C v3
