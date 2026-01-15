FROM python:3.10-slim

WORKDIR /app

# Copy the package files
COPY . .

# Install the package
RUN pip install --no-cache-dir .

# Default command: show help or run a demo
CMD ["python", "-c", "import star; star.pyramid(5)"]
