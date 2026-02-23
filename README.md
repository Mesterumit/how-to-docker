# Docker for AI/ML Bootcamp

A hands-on introduction to containerization for machine learning and data science workflows.

## 🚀 Quick Start

This tutorial is designed as a 30-45 minute hands-on introduction to Docker for AI/ML bootcamp students. It covers containerization fundamentals through three progressive examples, culminating in creating and publishing your own ML development environment.

## 📚 Tutorial Site

Visit the full tutorial at: **[GitHub Pages Site](https://siderealyear.github.io/how-to-docker/)**

## 📋 What You'll Learn

1. **Docker Basics**: Images, containers, Dockerfiles, and key concepts
2. **Building Containers**: From simple scripts to web applications
3. **Development Containers**: Creating portable, shareable ML development environments
4. **Publishing Images**: Sharing your work via Docker Hub
5. **Portability**: Verifying your environment works anywhere (GitHub Codespaces)

## 🎯 Learning Objectives

By the end of this tutorial, you will:

- ✅ Understand why containerization matters for ML engineering
- ✅ Build Docker images from Dockerfiles
- ✅ Run containerized applications with volume mounts and port mapping
- ✅ Create a VS Code development container for ML projects
- ✅ Publish container images to Docker Hub
- ✅ Launch your environment in GitHub Codespaces

## 📂 Repository Structure

```
.
├── index.md                  # Main tutorial content (GitHub Pages)
├── _config.yml              # GitHub Pages configuration
├── 01-data-cleaner/         # Example 1: Containerized data processing (3 min)
├── 02-streamlit-app/        # Example 2: Containerized web app (5 min)
└── 03-ml-dev-container/     # Example 3: ML dev environment (10 min)
```

## ⚡ Quick Examples

### Example 1: Data Cleaner (3 minutes)
Build a containerized pandas-based data cleaning script—a modular component for ML pipelines.

```bash
cd 01-data-cleaner
docker build -t data-cleaner .
docker run --rm -v "$(pwd)/data:/data" data-cleaner
```

### Example 2: Streamlit App (5 minutes)
Run an interactive data visualization dashboard in a container.

```bash
cd 02-streamlit-app
docker build -t streamlit-dashboard .
docker run --rm -p 8501:8501 streamlit-dashboard
# Visit http://localhost:8501
```

### Example 3: ML Dev Container (10 minutes)
Create, customize, and publish your own ML development environment.

```bash
cd 03-ml-dev-container
docker build -t ml-dev-env:v1.0 .
docker tag ml-dev-env:v1.0 YOUR_USERNAME/ml-dev-env:v1.0
docker push YOUR_USERNAME/ml-dev-env:v1.0
# Launch in GitHub Codespaces to verify!
```

## 🔧 Prerequisites

- Docker Desktop installed ([Get Docker](https://www.docker.com/products/docker-desktop/))
- Docker Hub account ([Sign up](https://hub.docker.com/signup))
- VS Code with Remote-Containers extension (optional but recommended)
- GitHub account (for Codespaces verification)
- Basic Python and command line knowledge

## 🌐 GitHub Pages Setup

To enable the tutorial website:

1. Go to repository Settings > Pages
2. Source: Deploy from a branch
3. Branch: `main` / root
4. Save

The site will be available at: `https://siderealyear.github.io/how-to-docker/`

## 🎓 For Instructors

This tutorial is designed for:
- **Duration**: 30-45 minute hands-on session
- **Audience**: AI/ML bootcamp students transitioning from notebooks to application development
- **Format**: Instructor-led demo with hands-on exercises
- **Completion goal**: Students build and publish their own dev container

### Suggested Timeline

- **5 min**: Introduction and prerequisites check
- **5 min**: Conceptual overview (why containers, production ML architecture)
- **3 min**: Example 1 walkthrough (data cleaner)
- **5 min**: Example 2 walkthrough (Streamlit app)
- **10 min**: Example 3 hands-on (dev container customization)
- **5 min**: Docker Hub publishing
- **5 min**: Codespaces verification
- **2-7 min**: Q&A and next steps

## 📖 Next Steps

After completing this tutorial, explore:

- **Docker Compose**: Multi-container applications (database + API + model)
- **Kubernetes**: Container orchestration for production ML systems
- **CI/CD**: Automated container building and deployment
- **Model Serving**: TensorFlow Serving, TorchServe in containers

## 🤝 Contributing

Found an issue or have a suggestion? Feel free to open an issue or submit a pull request!

## 📄 License

This tutorial is open source and available for educational use.
