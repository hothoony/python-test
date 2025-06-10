# Use an official Python runtime as a parent image
FROM python:3.9-slim as base

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONFAULTHANDLER=1 \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    POETRY_VERSION=1.5.1 \
    POETRY_HOME="/opt/poetry" \
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    POETRY_NO_INTERACTION=1 \
    PYSETUP_PATH="/opt/pysetup" \
    VENV_PATH="/opt/pysetup/.venv"

# Prepend poetry and venv to PATH
ENV PATH="$POETRY_HOME/bin:$VENV_PATH/bin:$PATH"

# Set work directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    curl \
    git \
    && rm -rf /var/lib/apt/lists/*

# Install Poetry
RUN curl -sSL https://install.python-poetry.org | python3 -


# Copy only requirements to cache them in docker layer
COPY pyproject.toml poetry.lock* ./


# Install runtime dependencies
RUN poetry install --no-interaction --no-ansi --without dev

# Copy the rest of the application
COPY . .


# Install the package in development mode
RUN poetry install --no-interaction --no-ansi

# Command to run the application
CMD ["python", "-m", "src.main"]

# Development stage
FROM base as development

# Install development dependencies
RUN poetry install --no-interaction --no-ansi

# Production stage
FROM base as production

# Copy only the installed packages from the development stage
COPY --from=base /app /app

# Set environment variables for production
ENV PYTHONPATH=/app \
    PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100

# Run as non-root user
RUN groupadd -r appuser && useradd -r -g appuser appuser
USER appuser

# Command to run the application
CMD ["python", "-m", "src.main"]
