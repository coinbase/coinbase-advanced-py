.PHONY: format, test
format:
	@echo "Formatting code..."
	isort .
	black .

test:
	@echo "Running tests..."
	python3 -m unittest discover -v