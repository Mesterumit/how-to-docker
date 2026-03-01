# Lab 2: Streamlit dashboard container

[Full Tutorial](https://gperdrizet.github.io/how-to-docker/lab-02-streamlit-app.html)

## Overview

An interactive Streamlit dashboard demonstrating containerized web applications.

**What you'll learn**: Port mapping, running web apps in containers, detached mode, and sharing interactive tools with your team.

## Quick start

```bash
cd 02-streamlit-app
docker build -t streamlit-dashboard .
docker run --rm -p 8501:8501 streamlit-dashboard
```

Then visit http://localhost:8501 in your browser.

## Files

- `app.py` - Interactive Streamlit dashboard with multiple visualizations
- `Dockerfile` - Container image with EXPOSE and ENV configuration
- `.dockerignore` - Build context exclusions

## For full step-by-step instructions

See the [complete tutorial](https://gperdrizet.github.io/how-to-docker/lab-02-streamlit-app.html) with detailed explanations, port mapping variations, and detached mode usage.
