# python-repo-template

A modern Python repository template with best practices and developer tooling pre-configured.

## Features

- **Package Management**: Uses `uv` for fast dependency resolution and management
- **Code Quality**: Pre-configured with multiple linters and formatters:
  - [Ruff](https://github.com/astral-sh/ruff) for linting and formatting
  - [Black](https://github.com/psf/black) for code formatting
  - [isort](https://github.com/PyCQA/isort) for import sorting
- **Pre-commit Hooks**: Automated code quality checks before commits
- **Testing**: [pytest](https://pytest.org/) setup for unit testing
- **Python Version**: Supports Python ≥3.13

## Quick Start

1. **Clone this template** (or use it as a GitHub template)
2. **Install dependencies**:
   ```bash
   uv sync --dev
   ```
3. **Install pre-commit hooks**:
   ```bash
   uv run pre-commit install
   ```
4. **Run tests**:
   ```bash
   uv run pytest
   ```

## Project Structure

```
src/           # Source code
tests/         # Test files
pyproject.toml # Project configuration and dependencies
uv.lock        # Locked dependency versions
```

## Development Workflow

The template includes automated code quality checks that run:
- On every commit (via pre-commit hooks)
- During CI/CD (GitHub Actions)

Code is automatically formatted and linted using Ruff, Black, and isort to maintain consistency.

## Getting Started with Your Project

1. Update the project name and description in [`pyproject.toml`](pyproject.toml)
2. Replace this README with your project's documentation
3. Start coding in the [`src/`](src/) directory
4. Add tests in the [`tests/`](tests/) directory
