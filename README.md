# Docker for AI/ML

A hands-on introduction to containerization for AI/ML.

## Quick start

This hands-on introduction to Docker for AI/ML (~1 hour) covers containerization fundamentals through three progressive labs, culminating in creating and publishing your own ML development environment.

## Tutorial site

Visit the full tutorial at: **[GitHub Pages Site](https://siderealyear.github.io/how-to-docker/)**

## What you'll learn

1. **Docker basics**: Images, containers, Dockerfiles, and key concepts
2. **Building containers**: From simple scripts to web applications
3. **Development containers**: Creating portable, shareable ML development environments
4. **Publishing images**: Sharing your work via Docker Hub
5. **Portability**: Verifying your environment works anywhere (GitHub Codespaces)

## Learning objectives

By the end of this tutorial, you will:

- Understand why containerization matters for ML engineering
- Build Docker images from Dockerfiles
- Run containerized applications with volume mounts and port mapping
- Create a VS Code development container for ML projects
- Publish container images to Docker Hub
- Launch your environment in GitHub Codespaces

## Repository structure

```text
.
├── docs/                    # Sphinx documentation source
│   ├── conf.py              # Sphinx configuration
│   ├── index.rst            # Documentation landing page
│   ├── overview.rst         # Tutorial overview
│   ├── concepts.rst         # Docker fundamentals
│   ├── dockerfile-guide.rst # Dockerfile reference
│   └── requirements.txt     # Sphinx build dependencies
├── .github/
│   └── workflows/
│       └── deploy-docs.yml  # GitHub Actions workflow for docs
├── 01-data-cleaner/         # Lab 1: Containerized data processing
├── 02-streamlit-app/        # Lab 2: Containerized web app
└── 03-ml-dev-container/     # Lab 3: ML dev environment
```

## Hands-on labs

### Lab 1: Data cleaner

Build a containerized Pandas-based data cleaning script - a modular component for ML pipelines.

```bash
cd 01-data-cleaner
docker build -t data-cleaner .
docker run --rm -v "$(pwd)/data:/data" data-cleaner
```

### Lab 2: Streamlit app

Run an interactive data visualization dashboard in a container.

```bash
cd 02-streamlit-app
docker build -t streamlit-dashboard .
docker run --rm -p 8501:8501 streamlit-dashboard
# Visit http://localhost:8501
```

### Lab 3: ML dev container

Create, customize, and publish your own ML development environment.

```bash
cd 03-ml-dev-container
docker build -t ml-dev-env:v1.0 .
docker tag ml-dev-env:v1.0 YOUR_USERNAME/ml-dev-env:v1.0
docker push YOUR_USERNAME/ml-dev-env:v1.0
# Launch in GitHub Codespaces to verify!
```

## Prerequisites

- Docker Desktop installed ([Get Docker](https://www.docker.com/products/docker-desktop/))
- Docker Hub account ([Sign up](https://hub.docker.com/signup))
- VS Code with Remote-Containers extension (optional but recommended)
- GitHub account (for Codespaces verification)
- Basic Python and command line knowledge

## GitHub Pages setup

To enable the tutorial website:

1. Go to repository Settings > Pages
2. Source: Deploy from a branch
3. Branch: `main` / root
4. Save

The site will be available at: `https://siderealyear.github.io/how-to-docker/`

## Building documentation locally

To build and preview the documentation on your local machine:

1. Create a Python virtual environment and install dependencies:

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r docs/requirements.txt
```

2. Build the documentation:

```bash
cd docs
sphinx-build -b html . _build/html
```

3. Serve the documentation locally:

```bash
cd _build/html
python -m http.server 8000
```

4. Open your browser and navigate to `http://localhost:8000`

The documentation will rebuild when you run `sphinx-build` again. To rebuild and view changes, repeat steps 2-4.

## Next steps

After completing this tutorial, explore:

- **Docker Compose**: Multi-container applications (database + API + model)
- **Kubernetes**: Container orchestration for production ML systems
- **CI/CD**: Automated container building and deployment
- **Model serving**: TensorFlow Serving, TorchServe in containers

## Contributing

Found an issue or have a suggestion? Feel free to open an issue or submit a pull request!

## License

This tutorial is open source and available for educational use.
