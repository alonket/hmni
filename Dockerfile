# Use Python 3.9 slim image as base
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy package files
COPY . .

# Install git (needed for abydos installation from GitHub)
RUN apt-get update && \
    apt-get install -y git && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Install package and dependencies (CPU-only PyTorch; avoids large CUDA wheels)
RUN pip install --no-cache-dir -e . \
    --index-url https://download.pytorch.org/whl/cpu \
    --extra-index-url https://pypi.org/simple

# Set Python path
ENV PYTHONPATH=/app

# Default command to run Python REPL
CMD ["python"] 