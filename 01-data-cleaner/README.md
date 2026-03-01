# Lab 1: Data cleaner container

[📚 Full Tutorial](https://gperdrizet.github.io/how-to-docker/lab-01-data-cleaner.html)

## Overview

A containerized pandas-based data cleaning script demonstrating modular ML pipeline components.

**What you'll learn**: Build your first Docker image, run containers with volume mounts, and see how containerization enables portable ML components.

## Quick start

```bash
cd 01-data-cleaner
docker build -t data-cleaner .
mkdir -p data/input data/output
cp sample_data.csv data/input/raw_data.csv
docker run --rm -v "$(pwd)/data:/data" data-cleaner
```

## Files

- `clean_data.py` - Pandas-based data cleaning script
- `Dockerfile` - Container image definition
- `sample_data.csv` - Sample dataset with common data quality issues
- `.dockerignore` - Build context exclusions

## For full step-by-step instructions

See the [complete tutorial](https://gperdrizet.github.io/how-to-docker/lab-01-data-cleaner.html) with detailed explanations and platform-specific commands.
