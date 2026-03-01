Lab 3: ML development container
================================

.. note::
   
   📁 `View lab files on GitHub <https://github.com/siderealyear/how-to-docker/tree/main/03-ml-dev-container>`_

Learning objectives
-------------------

- Build and customize a Docker image for ML development
- Tag Docker images with semantic versioning
- Publish images to Docker Hub
- Use a pre-built image as a VS Code development container
- Verify portability by launching in GitHub Codespaces
- Understand how dev containers enable team collaboration

What's included
---------------

- ``.devcontainer/devcontainer.json``: VS Code dev container configuration
- ``Dockerfile``: Container image definition with Python, git, and minimal ML packages
- ``requirements.txt``: Python dependencies (starter set for customization)
- ``test_environment.py``: Script to verify your setup works
- ``.dockerignore``: Files to exclude from builds

The scenario
------------

You're starting a new ML project with your team. Instead of everyone spending hours setting up Python, installing packages, and debugging dependency conflicts, you'll:

1. Create a standardized development container
2. Customize it with your preferred ML tools
3. Publish it to Docker Hub
4. Share it with your team (and verify it works in Codespaces)

From now on, anyone can start developing in seconds with the exact same environment.

Part 1: Build and test your development image
----------------------------------------------

1. Examine the Dockerfile
~~~~~~~~~~~~~~~~~~~~~~~~~~

Navigate to the example directory and open the Dockerfile:

.. code-block:: bash

   cd 03-ml-dev-container

Notice the structure - similar to labs 1 and 2, but designed for development:

.. code-block:: dockerfile

   FROM python:3.11-slim
   WORKDIR /workspace
   RUN apt-get update && apt-get install -y git curl && rm -rf /var/lib/apt/lists/*
   RUN pip install --no-cache-dir --upgrade pip
   RUN pip install --no-cache-dir pandas numpy scikit-learn
   RUN useradd -m -s /bin/bash devuser && chown -R devuser:devuser /workspace
   USER devuser
   ENV PYTHONUNBUFFERED=1 PYTHONDONTWRITEBYTECODE=1
   CMD ["/bin/bash"]

**New concepts**:

- ``apt-get install``: Installing system packages (git, curl) not just Python packages
- ``useradd``: Creating a non-root user for security
- ``USER``: Switching to that user
- ``CMD ["/bin/bash"]``: Opens a shell instead of running a specific script

2. Build the image
~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   docker build -t ml-dev-env .

This builds your development environment image.

3. Test the environment
~~~~~~~~~~~~~~~~~~~~~~~

Run the test script to verify everything works:

.. tab-set::

   .. tab-item:: Linux/macOS

      .. code-block:: bash

         docker run --rm -v "$(pwd):/workspace" ml-dev-env python test_environment.py

   .. tab-item:: Windows PowerShell

      .. code-block:: powershell

         docker run --rm -v "${PWD}:/workspace" ml-dev-env python test_environment.py

   .. tab-item:: Windows CMD

      .. code-block:: batch

         docker run --rm -v "%cd%:/workspace" ml-dev-env python test_environment.py

You should see output training a classifier on the iris dataset. If it works, your base environment is ready!

4. Try interactive development
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Run the container interactively:

.. tab-set::

   .. tab-item:: Linux/macOS

      .. code-block:: bash

         docker run --rm -it -v "$(pwd):/workspace" ml-dev-env

   .. tab-item:: Windows PowerShell

      .. code-block:: powershell

         docker run --rm -it -v "${PWD}:/workspace" ml-dev-env

   .. tab-item:: Windows CMD

      .. code-block:: batch

         docker run --rm -it -v "%cd%:/workspace" ml-dev-env

You're now inside the container with a bash shell! Try:

- ``python --version``
- ``pip list``
- ``python test_environment.py``

Type ``exit`` to leave the container.

Part 2: Customize your environment
-----------------------------------

5. Add your preferred packages
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Edit ``requirements.txt`` to add packages you use regularly. Some suggestions:

.. code-block:: text

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

Add a ``RUN`` command to the Dockerfile to install these:

.. code-block:: dockerfile

   # After the existing pip install line, add:
   COPY requirements.txt .
   RUN pip install --no-cache-dir -r requirements.txt

6. Rebuild with customizations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   docker build -t ml-dev-env:v1.0 .

Note: We're now tagging with a version number using semantic versioning!

Part 3: Publish to Docker Hub
------------------------------

7. Tag for Docker Hub
~~~~~~~~~~~~~~~~~~~~~

Replace ``YOUR_DOCKERHUB_USERNAME`` with your actual username:

.. code-block:: bash

   docker tag ml-dev-env:v1.0 YOUR_DOCKERHUB_USERNAME/ml-dev-env:v1.0
   docker tag ml-dev-env:v1.0 YOUR_DOCKERHUB_USERNAME/ml-dev-env:latest

**Understanding tags**:

- ``v1.0``: Specific version (semantic versioning)
- ``latest``: Convention for the most recent stable version
- Best practice: Push both so users can pin to a version or use latest

8. Login to Docker Hub
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   docker login

Enter your Docker Hub credentials when prompted.

9. Push to Docker Hub
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   docker push YOUR_DOCKERHUB_USERNAME/ml-dev-env:v1.0
   docker push YOUR_DOCKERHUB_USERNAME/ml-dev-env:latest

This uploads your image to Docker Hub, making it publicly accessible!

10. Verify on Docker Hub
~~~~~~~~~~~~~~~~~~~~~~~~~

Visit ``https://hub.docker.com/r/YOUR_DOCKERHUB_USERNAME/ml-dev-env`` to see your published image.

Part 4: Use your image as a VS Code dev container
--------------------------------------------------

**New concept**: Instead of running containers manually, VS Code can use your image as a complete development environment with your editor, extensions, and tools integrated.

11. Examine the dev container configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Open ``.devcontainer/devcontainer.json``:

.. code-block:: json

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

**Key elements**:

- ``dockerfile``: Points to your Dockerfile (uses the image you just built)
- ``extensions``: VS Code extensions to auto-install in the container
- ``forwardPorts``: Ports to expose (Jupyter: 8888, Streamlit: 8501)
- ``remoteUser``: Run as the non-root user you created

12. Open in VS Code dev container (optional)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you have VS Code with the Remote-Containers extension:

1. Open this folder in VS Code
2. Press ``F1`` (or ``Cmd/Ctrl+Shift+P``)
3. Select "Dev Containers: Reopen in Container"
4. Wait for VS Code to reload

VS Code now runs inside your container! Any code you write, any terminal commands you run, all happen in the containerized environment. But it feels like normal VS Code.

Part 5: Verify portability with GitHub Codespaces
--------------------------------------------------

Now for the ultimate test: proving your environment works anywhere!

13. Create a test repository
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Create a new GitHub repository with just these files:

.. code-block:: text

   my-ml-project/
   ├── .devcontainer/
   │   └── devcontainer.json
   └── README.md

In ``.devcontainer/devcontainer.json``, reference your published image:

.. code-block:: json

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
     "forwardPorts": [8888, 8501]
   }

Note: Instead of ``"build": {"dockerfile": "Dockerfile"}``, we now use ``"image"`` pointing to your published image!

14. Launch GitHub Codespace
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Go to your repository on GitHub
2. Click the green "Code" button
3. Select "Codespaces" tab
4. Click "Create codespace on main"

GitHub will:

- Pull your published image from Docker Hub
- Create a cloud-based development environment
- Launch VS Code in your browser
- Have your exact environment ready in ~30 seconds!

15. Test in Codespace
~~~~~~~~~~~~~~~~~~~~~

In the Codespace terminal, verify your environment:

.. code-block:: bash

   python --version
   pip list

You should see all your customized packages installed. Try creating a Python file and running some code!

**Success!** You've proven your development environment is:

- Reproducible (same packages everywhere)
- Portable (runs locally and in the cloud)
- Shareable (anyone can use it via Docker Hub)
- Collaborative (team members get identical setups)

Key concepts
------------

- **Building development images**: Creating containers optimized for coding, not just running apps
- **Image tagging**: Versioning with semantic tags (v1.0) and latest
- **Docker Hub**: Publishing and sharing container images
- **Dev containers**: Using Docker images as complete VS Code development environments
- **Portability**: The same environment runs locally, in VS Code, in Codespaces, on teammates' machines
- **Customization**: Tailoring environments to your workflow
- **Collaboration**: Eliminating "works on my machine" problems forever

Real-world ML applications
---------------------------

This dev container pattern is used by:

- **ML teams** for consistent training environments
- **Data science teams** for reproducible analyses
- **Open source projects** so contributors have identical setups
- **Bootcamps and courses** to eliminate setup problems
- **Production pipelines** where training containers match dev environments exactly

Alternative registries
----------------------

While this tutorial uses Docker Hub, you can publish to:

**GitHub Container Registry (ghcr.io)**:

.. code-block:: bash

   docker tag ml-dev-env:v1.0 ghcr.io/YOUR_USERNAME/ml-dev-env:v1.0
   docker push ghcr.io/YOUR_USERNAME/ml-dev-env:v1.0

**AWS Elastic Container Registry (ECR)**: For AWS deployments

**Google Container Registry (GCR)**: For Google Cloud

**Azure Container Registry (ACR)**: For Azure deployments

The workflow is the same—just different registry URLs!

Experiment further
------------------

1. **Add a Jupyter server**: Modify the Dockerfile to include ``CMD ["jupyter", "lab"]``
2. **Create team variants**: Make specialized containers (computer vision, NLP, time series)
3. **Version iterations**: Make changes, tag as ``v1.1``, and push
4. **Share with classmates**: Have someone pull your image and verify it works
5. **Add data science tools**: Include DVC, MLflow, or Weights & Biases

Troubleshooting
---------------

**Build fails**: Check Dockerfile syntax, ensure package names are correct

**Extensions don't install**: Verify extension IDs are correct in devcontainer.json

**Port forwarding doesn't work**: Check ``forwardPorts`` array includes the port you need

**Codespace fails to create**: Verify image name in devcontainer.json matches Docker Hub exactly

**Push to Docker Hub fails**: Ensure you're logged in and have the correct permissions

What you've accomplished
------------------------

- Created a professional ML development container
- Customized it with your preferred tools and extensions
- Published your first Docker image to a public registry
- Verified portability by launching in GitHub Codespaces
- Learned the foundation for collaborative, reproducible ML workflows

Next steps
----------

You're now ready to:

- Use this dev container for your course projects
- Explore **Docker Compose** for multi-container setups (database + app + model server)
- Learn about **Kubernetes** for orchestrating containers in production
- Build containers for model training and serving
- Create CI/CD pipelines that build and push containers automatically

---

**Congratulations!** You've completed the Docker tutorial. You now understand containerization fundamentals and have a production-ready development environment published and ready to use!
