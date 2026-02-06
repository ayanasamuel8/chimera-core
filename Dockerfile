# Use a slim professional image
FROM python:3.12-slim-bookworm

# Set working directory
WORKDIR /app

# Install uv for fast package management
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/uv

# Copy dependency files
COPY pyproject.toml .
COPY uv.lock .

# Install dependencies
RUN uv sync --frozen

# Copy source code
COPY . .

# Default command: Run tests
CMD ["uv", "run", "pytest", "tests/"]