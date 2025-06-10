# Python Project Template

A production-ready Python project template following best practices.

## Features

- Modern Python project structure
- Pre-configured development tools (black, isort, mypy, flake8, pytest)
- Type checking with mypy
- Code formatting with black and isort
- Linting with flake8
- Testing with pytest
- Pre-commit hooks
- GitHub Actions CI/CD
- Docker support
- Logging configuration
- Environment variable management

## Prerequisites

- Python 3.9+
- pip
- Git
- (Optional) Docker

## Getting Started

### Local Development

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/python-project-template.git
   cd python-project-template
   ```

2. Set up the development environment:
   ```bash
   make setup
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. Install development dependencies:
   ```bash
   make install-dev
   ```

4. Run the application:
   ```bash
   make run
   ```

### Running Tests

```bash
make test
```

### Code Quality

- Format code:
  ```bash
  make format
  ```

- Lint code:
  ```bash
  make lint
  ```

- Type checking:
  ```bash
  make typecheck
  ```

## Project Structure

```
.
├── .github/                # GitHub configurations
│   └── workflows/          # GitHub Actions workflows
├── docker/                 # Docker configurations
├── docs/                   # Documentation files
├── src/                    # Source code
│   └── project_name/       # Main package
│       ├── __init__.py
│       ├── main.py
│       └── config.py       # Configuration management
├── tests/                  # Test files
├── .env.example            # Example environment variables
├── .flake8                 # Flake8 configuration
├── .gitignore
├── .pre-commit-config.yaml # Pre-commit hooks
├── Makefile                # Project commands
├── pyproject.toml          # Project metadata and dependencies
├── README.md               # This file
└── requirements-dev.txt    # Development dependencies
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.