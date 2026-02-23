# Use Python 3.11 slim as base image
FROM python:3.11-slim

# Set working directory
WORKDIR /workspace

# Install system dependencies
RUN apt-get update && apt-get install -y \
    git \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Upgrade pip
RUN pip install --no-cache-dir --upgrade pip

# Install minimal Python packages for ML development
# Students will add more packages as part of the exercise
RUN pip install --no-cache-dir \
    pandas \
    numpy \
    scikit-learn

# Create a non-root user for development
RUN useradd -m -s /bin/bash devuser && \
    chown -R devuser:devuser /workspace

# Switch to non-root user
USER devuser

# Set Python environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

# Default command opens a bash shell
CMD ["/bin/bash"]
