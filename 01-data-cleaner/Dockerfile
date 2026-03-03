# Use Python 3.11 slim image as base
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install pandas
RUN pip install --no-cache-dir pandas

# Copy the cleaning script ,"." means into current working directory
COPY clean_data.py . 

# Create directories for data
RUN mkdir -p /data/input /data/output

# Run the script by default
CMD ["python", "clean_data.py"]
