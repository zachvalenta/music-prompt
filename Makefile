.PHONY: test export

help:
	@echo
	@echo "======================================================================"
	@echo
	@echo "test:      output sample data"
	@echo "chords:    output chords"
	@echo "melody:    output melody"
	@echo
	@echo "======================================================================"
	@echo

test:
	poetry run python test.py

chords:
	poetry run python chords.py

melody:
	poetry run python melody.py
