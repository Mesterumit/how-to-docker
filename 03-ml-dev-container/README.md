# Lab 3: ML development container

[Full Tutorial](https://gperdrizet.github.io/how-to-docker/lab-03-ml-dev-container.html)

## Overview

Create a customizable ML development environment, publish it to Docker Hub, and verify it works everywhere.

**What you'll learn**: Building dev containers, semantic versioning, publishing to registries, VS Code dev containers, and GitHub Codespaces.

## Quick start

```bash
cd 03-ml-dev-container
docker build -t ml-dev-env:v1.0 .
docker run --rm -v "$(pwd):/workspace" ml-dev-env python test_environment.py
```

## Files

- `Dockerfile` - Development-optimized container with Python, git, and ML packages
- `.devcontainer/devcontainer.json` - VS Code dev container configuration
- `requirements.txt` - Customizable Python dependencies
- `test_environment.py` - Environment verification script
- `.dockerignore` - Build context exclusions

## Tutorial structure

The [complete tutorial](https://gperdrizet.github.io/how-to-docker/lab-03-ml-dev-container.html) walks through:

- **Part 1**: Build and test your development image
- **Part 2**: Customize with your preferred ML packages
- **Part 3**: Publish to Docker Hub with semantic versioning
- **Part 4**: Use as a VS Code dev container
- **Part 5**: Launch in GitHub Codespaces to verify portability

## For full step-by-step instructions

See the [complete tutorial](https://gperdrizet.github.io/how-to-docker/lab-03-ml-dev-container.html) with detailed explanations, platform-specific commands, and configuration examples.
