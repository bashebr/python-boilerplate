.PHONY: lint format typecheck test dev start all

lint:
	uv run ruff check .

format:
	uv run ruff format .

typecheck:
	uv run mypy src

test:
	uv run pytest --cov=python_boilerplate

dev:
	uv run python src/python_boilerplate/cli.py

start:
	uv run uvicorn python_boilerplate.web:app --reload

all: lint typecheck test