.PHONY: test export

help:
	@echo
	@echo "======================================================================"
	@echo
	@echo "test:      output sample data"
	@echo
	@echo "======================================================================"
	@echo

test:
	poetry run python test.py

