# Python Boilerplate

> A clean, modern, senior-grade Python project template powered by [uv](https://github.com/astral-sh/uv).

This repository gives you a production-ready starting point for CLI tools, FastAPI services, libraries, or micro-SaaS apps. It favors convention over guesswork so every new project begins with the same quality bar, tooling, and developer experience.

## Highlights

- Lightweight, framework-agnostic structure that you can clone and rename in seconds
- Strict typing, formatting, and linting baked in (mypy + Ruff + pytest + coverage)
- uv manages dependencies, virtualenvs, and ad-hoc tooling via `uv run <command>`
- Ready-to-ship CI/CD (lint → type-check → tests, dependency updates, semantic release)
- Docker + Docker Compose for local and production parity
- Bootstrap script resets metadata, git history, and naming for a fresh project

## Quick Start

1. Clone the template
   ```bash
   git clone <this-repo> myproject
   cd myproject
   ```
2. Bootstrap your new name/metadata
   ```bash
   ./scripts/bootstrap.sh myproject
   ```
3. Install dependencies
   ```bash
   uv sync
   ```
4. Start building
   ```bash
   uv run python src/python_boilerplate/cli.py      # Typer CLI entrypoint
   uv run uvicorn python_boilerplate.web:app --reload  # FastAPI app @ http://127.0.0.1:8000
   uv run pytest                                    # pytest + coverage
   ```

## Development Commands

Run common workflows through uv commands for consistent automation:

| Command | Description |
| --- | --- |
| `uv run ruff check .` | Ruff linting |
| `uv run ruff format .` | Ruff formatting |
| `uv run mypy src` | mypy type checking |
| `uv run pytest --cov=python_boilerplate` | pytest with coverage |
| `uv run python src/python_boilerplate/cli.py` | Execute the Typer CLI |
| `uv run uvicorn python_boilerplate.web:app --reload` | Launch the FastAPI server |
| `uv run ruff check . && uv run mypy src && uv run pytest` | lint + mypy + tests |

## Project Layout

```text
src/
  python_boilerplate/
    cli.py             # Typer CLI
    web.py             # FastAPI app
    config.py          # Pydantic settings
    logging_config.py  # Centralized logging
scripts/
  bootstrap.sh        # Renames project + resets git history
.github/
docker/
tests/
```

## Batteries Included

- **Modern tooling:** uv, `pyproject.toml`, Ruff, mypy, pytest, pre-commit hooks
- **Application ready:** Typer CLI, FastAPI server, centralized config/logging, Docker + Compose
- **Production CI/CD:** GitHub Actions for lint → type-check → tests, dependency updates, optional semantic versioning
- **Automation:** Daily schedule to run `uv lock --upgrade` and raise pull requests so dependencies stay fresh

## Bootstrap Script

Bring any new project to life fast:

```bash
./scripts/bootstrap.sh <new_project_name>
```

The script renames folders, updates `pyproject` metadata, resets git history, and leaves you with a pristine repo ready for your team.

## When to Use This Template

Ideal for:

- Python CLI tools, automation scripts, or internal utilities
- FastAPI microservices and micro-SaaS products
- Libraries, SDKs, data/ETL jobs, and other backend services

Every project keeps the same structure, tooling, CI gates, and developer experience—making long-term maintenance straightforward.

## Keeping Dependencies Fresh

A scheduled GitHub Action runs daily to:

1. Execute `uv lock --upgrade`
2. Open a pull request with updated pins
3. Ensure the template stays secure and modern

## License

MIT — free for private or commercial use.
