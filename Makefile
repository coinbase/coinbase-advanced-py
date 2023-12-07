.PHONY: format
format:
	@echo "Formatting code..."
	isort .
	black .