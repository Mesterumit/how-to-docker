# Example 3: ML development container

**Time to complete**: ~10 minutes

## Learning objectives

- Create a VS Code development container
- Customize a dev environment for ML work
- Build and tag Docker images with semantic versioning
- Publish images to Docker Hub
- Verify portability by launching in GitHub Codespaces
- Understand how dev containers enable team collaboration

## What's included

- `.devcontainer/devcontainer.json`: VS Code dev container configuration
- `Dockerfile`: Container image definition with Python, git, and minimal ML packages
- `requirements.txt`: Python dependencies (starter set for customization)
- `test_environment.py`: Script to verify your setup works
- `.dockerignore`: Files to exclude from builds

## The scenario

You're starting a new ML project with your team. Instead of everyone spending hours setting up Python, installing packages, and debugging dependency conflicts, you'll:

1. Create a standardized development container
2. Customize it with your preferred ML tools
3. Publish it to Docker Hub
4. Share it with your team (and verify it works in Codespaces)

From now on, anyone can start developing in seconds with the exact same environment.

## Step-by-step instructions

### Part 1: Build and test locally (3 minutes)

#### 1. Examine the Dev Container Configuration

Open `.devcontainer/devcontainer.json`. This file tells VS Code how to create your development environment:

```json
{
  "name": "ML Development Environment",
  "build": {
    "dockerfile": "Dockerfile"
  },
  "customizations": {
    "vscode": {
      "extensions": ["ms-python.python", "ms-python.vscode-pylance"]
    }
  },
  "forwardPorts": [8888, 8501],
  "postCreateCommand": "pip install --user -r requirements.txt",
  "remoteUser": "devuser"
}
```

**Key elements**:
- `dockerfile`: Points to the Dockerfile to build
- `extensions`: VS Code extensions to auto-install
- `forwardPorts`: Ports to expose (Jupyter: 8888, Streamlit: 8501)
- `postCreateCommand`: Runs after container creation
- `remoteUser`: Non-root user for security

#### 2. Open in Container (VS Code Users)

If you have VS Code with the Remote-Containers extension:

1. Open this folder in VS Code
2. Press `F1` (or `Cmd/Ctrl+Shift+P`)
3. Select "Dev Containers: Reopen in Container"
4. Wait for the container to build (first time takes ~2 minutes)

VS Code will reload inside the container!

**OR** continue with manual Docker commands below.

#### 3. Build the image manually

```bash
docker build -t ml-dev-env .
```

#### 4. Test the Environment

Run the test script:

```bash
docker run --rm -v "$(pwd):/workspace" ml-dev-env python test_environment.py
```

You should see output training a classifier on the iris dataset. If it works, your base environment is ready!

### Part 2: Customize your environment (3 minutes)

#### 5. Add your preferred packages

Edit `requirements.txt` to add packages you use regularly. Some suggestions:

```txt
# Visualization
matplotlib>=3.7.0
seaborn>=0.12.0
plotly>=5.14.0

# Jupyter
jupyter>=1.0.0
jupyterlab>=4.0.0

# Deep Learning (choose one or both)
tensorflow>=2.12.0
torch>=2.0.0
torchvision>=0.15.0

# Additional ML
xgboost>=1.7.0
lightgbm>=4.0.0

# Utilities
python-dotenv>=1.0.0
tqdm>=4.65.0
```

#### 6. Add VS Code Extensions

Edit `.devcontainer/devcontainer.json` to add more extensions:

```json
"extensions": [
  "ms-python.python",
  "ms-python.vscode-pylance",
  "ms-toolsai.jupyter",
  "ms-toolsai.vscode-jupyter-cell-tags",
  "ms-toolsai.vscode-jupyter-slideshow",
  "esbenp.prettier-vscode",
  "eamodio.gitlens"
]
```

Some popular extensions for ML:
- `ms-toolsai.jupyter`: Jupyter notebook support
- `donjayamanne.githistory`: Git history visualization  
- `visualstudioexptteam.vscodeintellicode`: AI-assisted coding
- `streetsidesoftware.code-spell-checker`: Spell checker

#### 7. Rebuild with Customizations

```bash
docker build -t ml-dev-env:v1.0 .
```

Note: We're now tagging with a version number!

### Part 3: Publish to Docker Hub (2 minutes)

#### 8. Tag for Docker Hub

Replace `YOUR_DOCKERHUB_USERNAME` with your actual username:

```bash
docker tag ml-dev-env:v1.0 YOUR_DOCKERHUB_USERNAME/ml-dev-env:v1.0
docker tag ml-dev-env:v1.0 YOUR_DOCKERHUB_USERNAME/ml-dev-env:latest
```

**Understanding tags**:
- `v1.0`: Specific version (semantic versioning)
- `latest`: Convention for the most recent stable version
- Best practice: Push both so users can pin to a version or use latest

#### 9. Login to Docker Hub

```bash
docker login
```

Enter your Docker Hub credentials when prompted.

#### 10. Push to Docker Hub

```bash
docker push YOUR_DOCKERHUB_USERNAME/ml-dev-env:v1.0
docker push YOUR_DOCKERHUB_USERNAME/ml-dev-env:latest
```

This uploads your image to Docker Hub, making it publicly accessible!

#### 11. Verify on Docker Hub

Visit `https://hub.docker.com/r/YOUR_DOCKERHUB_USERNAME/ml-dev-env` to see your published image.

### Part 4: Verify portability with GitHub Codespaces (2 minutes)

Now for the ultimate test: proving your environment works anywhere!

#### 12. Create a test repository

Create a new GitHub repository with just these files:

```
my-ml-project/
├── .devcontainer/
│   └── devcontainer.json
└── README.md
```

In `.devcontainer/devcontainer.json`, reference your published image:

```json
{
  "name": "ML Dev Environment from Docker Hub",
  "image": "YOUR_DOCKERHUB_USERNAME/ml-dev-env:v1.0",
  "customizations": {
    "vscode": {
      "extensions": [
        "ms-python.python",
        "ms-python.vscode-pylance"
      ]
    }
  },
  "forwardPorts": [8888, 8501],
  "postCreateCommand": "echo '🎉 Environment ready!'"
}
```

#### 13. Launch GitHub Codespace

1. Go to your repository on GitHub
2. Click the green "Code" button
3. Select "Codespaces" tab
4. Click "Create codespace on main"

GitHub will:
- Pull your published image from Docker Hub
- Create a cloud-based development environment
- Launch VS Code in your browser
- Have your exact environment ready in ~30 seconds!

#### 14. Test in Codespace

In the Codespace terminal, verify your environment:

```bash
python --version
pip list
```

You should see all your customized packages installed. Try creating a Python file and running some code!

**Success!** You've proven your development environment is:
- Reproducible (same packages everywhere)
- Portable (runs locally and in the cloud)
- Shareable (anyone can use it via Docker Hub)
- Collaborative (team members get identical setups)

## Key concepts reinforced

- **Dev containers**: Complete development environments as code
- **Image tagging**: Versioning with semantic tags (v1.0) and latest
- **Docker Hub**: Publishing and sharing container images
- **Portability**: The same environment runs locally, in Codespaces, on teammates' machines
- **Customization**: Tailoring environments to your workflow
- **Collaboration**: Eliminating "works on my machine" problems forever

## Real-world ML applications

This dev container pattern is used by:

- **ML teams** for consistent training environments
- **Data science teams** for reproducible analyses  
- **Open source projects** so contributors have identical setups
- **Bootcamps and courses** to eliminate setup problems
- **Production pipelines** where training containers match dev environments exactly

## Alternative registries

While this tutorial uses Docker Hub, you can publish to:

- **GitHub Container Registry** (ghcr.io):
  ```bash
  docker tag ml-dev-env:v1.0 ghcr.io/YOUR_USERNAME/ml-dev-env:v1.0
  docker push ghcr.io/YOUR_USERNAME/ml-dev-env:v1.0
  ```

- **AWS Elastic Container Registry** (ECR): For AWS deployments

- **Google Container Registry** (GCR): For Google Cloud

- **Azure Container Registry** (ACR): For Azure deployments

The workflow is the same—just different registry URLs!

## Experiment further

1. **Add a Jupyter server**: Modify the Dockerfile to include `CMD ["jupyter", "lab"]`
2. **Create team variants**: Make specialized containers (computer vision, NLP, time series)
3. **Version iterations**: Make changes, tag as `v1.1`, and push
4. **Share with classmates**: Have someone pull your image and verify it works
5. **Add data science tools**: Include DVC, MLflow, or Weights & Biases

## Troubleshooting

**Build fails**: Check Dockerfile syntax, ensure package names are correct

**Extensions don't install**: Verify extension IDs are correct in devcontainer.json

**Port forwarding doesn't work**: Check `forwardPorts` array includes the port you need

**Codespace fails to create**: Verify image name in devcontainer.json matches Docker Hub exactly

**Push to Docker Hub fails**: Ensure you're logged in and have the correct permissions

## What you've accomplished

- Created a professional ML development container
- Customized it with your preferred tools and extensions
- Published your first Docker image to a public registry
- Verified portability by launching in GitHub Codespaces
- Learned the foundation for collaborative, reproducible ML workflows

## Next steps

You're now ready to:

- Use this dev container for your course projects
- Explore **Docker Compose** for multi-container setups (database + app + model server)
- Learn about **Kubernetes** for orchestrating containers in production
- Build containers for model training and serving
- Create CI/CD pipelines that build and push containers automatically

---

**Time check**: This example targets 10 minutes total:
- Part 1 (Build & test): ~3 min
- Part 2 (Customize): ~3 min  
- Part 3 (Publish): ~2 min
- Part 4 (Codespaces): ~2 min

**Congratulations!** You've completed the Docker tutorial. You now understand containerization fundamentals and have a production-ready development environment published and ready to use!
