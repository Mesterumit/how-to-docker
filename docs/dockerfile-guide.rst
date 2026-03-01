Dockerfile guide
================

A Dockerfile contains instructions executed in order to build an image. Understanding these instructions is key to creating effective containerized applications.

Essential instructions
----------------------

FROM
~~~~

Specifies the base image to build upon.

.. code-block:: dockerfile

   FROM python:3.11-slim

**Best practice**: Use specific tags (``3.11-slim``) instead of ``latest`` for reproducibility.

WORKDIR
~~~~~~~

Sets the working directory inside the container. All subsequent commands run from this directory.

.. code-block:: dockerfile

   WORKDIR /app

**Tip**: Creates the directory if it doesn't exist.

COPY
~~~~

Copies files from your host machine to the container.

.. code-block:: dockerfile

   COPY requirements.txt /app/
   COPY . /app

**Pattern**: Copy dependencies first, then code (for better caching).

RUN
~~~

Executes commands during the image build process. Commonly used to install dependencies.

.. code-block:: dockerfile

   RUN pip install --no-cache-dir -r requirements.txt

**Best practice**: Combine related commands with ``&&`` to reduce layers.

CMD
~~~

Specifies the default command to run when a container starts.

.. code-block:: dockerfile

   CMD ["python", "app.py"]

**Note**: Only one ``CMD`` per Dockerfile. Easily overridden at runtime.

**Important**: Containers run as long as the command is running. When the command exits, the container stops. If you don't specify a ``CMD`` (or run with ``-it`` for interactive mode), the container will start and immediately exit. For long-running services like web apps, the ``CMD`` should start a server that keeps running. For batch jobs, the container exits when processing completes.

EXPOSE
~~~~~~

Documents which ports the container listens on.

.. code-block:: dockerfile

   EXPOSE 8080

**Important**: This doesn't actually publish the port - use ``-p`` when running.

ENV
~~~

Sets environment variables.

.. code-block:: dockerfile

   ENV PYTHONUNBUFFERED=1
   ENV MODEL_PATH=/models

USER
~~~~

Sets the user for running subsequent commands.

.. code-block:: dockerfile

   RUN useradd -m appuser
   USER appuser

**Security**: Never run as root in production!

Complete example
----------------

Here's a well-structured Dockerfile for an ML application:

.. code-block:: dockerfile

   # Use specific Python version
   FROM python:3.11-slim

   # Set working directory
   WORKDIR /app

   # Install system dependencies
   RUN apt-get update && apt-get install -y \
       git \
       curl \
       && rm -rf /var/lib/apt/lists/*

   # Copy and install Python dependencies first (for caching)
   COPY requirements.txt .
   RUN pip install --no-cache-dir -r requirements.txt

   # Copy application code
   COPY . .

   # Create non-root user
   RUN useradd -m -s /bin/bash mluser && \
       chown -R mluser:mluser /app
   USER mluser

   # Set environment variables
   ENV PYTHONUNBUFFERED=1

   # Expose port
   EXPOSE 8000

   # Run application
   CMD ["python", "app.py"]

Best practices
--------------

Layer caching
~~~~~~~~~~~~~

Docker caches each layer. Order instructions from least to most frequently changing:

.. code-block:: dockerfile

   # ✅ Good - dependencies change less often than code
   FROM python:3.11-slim
   COPY requirements.txt .
   RUN pip install -r requirements.txt
   COPY . .

   # ❌ Bad - code changes invalidate dependency cache
   FROM python:3.11-slim
   COPY . .
   RUN pip install -r requirements.txt

Minimize layers
~~~~~~~~~~~~~~~

Combine related ``RUN`` commands:

.. code-block:: dockerfile

   # ✅ Good - one layer
   RUN apt-get update && \
       apt-get install -y git curl && \
       rm -rf /var/lib/apt/lists/*

   # ❌ Bad - three layers
   RUN apt-get update
   RUN apt-get install -y git curl
   RUN rm -rf /var/lib/apt/lists/*

Use .dockerignore
~~~~~~~~~~~~~~~~~

Exclude unnecessary files from the build context:

.. code-block:: text

   # .dockerignore
   __pycache__/
   *.pyc
   .git/
   .venv/
   *.md
   .DS_Store

Keep images small
~~~~~~~~~~~~~~~~~

.. code-block:: dockerfile

   # Use slim/alpine variants
   FROM python:3.11-slim  # ~120 MB
   # vs
   FROM python:3.11       # ~900 MB

   # Clean up in same layer
   RUN apt-get update && \
       apt-get install -y curl && \
       rm -rf /var/lib/apt/lists/*

   # Use --no-cache-dir with pip
   RUN pip install --no-cache-dir pandas

Specific tags
~~~~~~~~~~~~~

.. code-block:: dockerfile

   # ✅ Good - reproducible
   FROM python:3.11.5-slim

   # ❌ Bad - breaks when "latest" updates
   FROM python:latest

Security
~~~~~~~~

.. code-block:: dockerfile

   # Create and use non-root user
   RUN groupadd -r appgroup && \
       useradd -r -g appgroup appuser
   USER appuser

   # Don't expose unnecessary ports
   # Only EXPOSE what's needed

Multi-stage builds
------------------

Multi-stage builds allow you to use multiple ``FROM`` statements in a single Dockerfile. Each stage can use a different base image and you can selectively copy artifacts from one stage to another, leaving behind everything you don't need in the final image.

**Why use multi-stage builds:**

- **Smaller production images**: Build dependencies (compilers, dev tools) stay in build stage, only runtime files go to production
- **Security**: Reduce attack surface by excluding build tools and source code from final image
- **Build optimization**: Use full-featured images for building, slim images for running
- **Separation of concerns**: Keep build logic separate from runtime configuration

**Common use case**: You need ``gcc``, ``make``, or other build tools to compile dependencies, but don't want them in your production image.

Example for smaller production images:

.. code-block:: dockerfile

   # Build stage - uses full Python image with build tools
   FROM python:3.11 AS builder
   WORKDIR /app
   COPY requirements.txt .
   # Install packages to user's local directory
   RUN pip install --user --no-cache-dir -r requirements.txt

   # Production stage - uses slim image (120MB vs 900MB)
   FROM python:3.11-slim
   WORKDIR /app
   # Copy only installed packages from builder stage
   COPY --from=builder /root/.local /root/.local
   # Copy application code
   COPY . .
   ENV PATH=/root/.local/bin:$PATH
   CMD ["python", "app.py"]

**Result**: Final image is ~300MB instead of ~1.2GB, includes only runtime dependencies, no pip cache or build tools.

Common patterns
---------------

ML training container
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: dockerfile

   FROM pytorch/pytorch:2.0.1-cuda11.7-cudnn8-runtime
   WORKDIR /workspace
   
   COPY requirements.txt .
   RUN pip install --no-cache-dir -r requirements.txt
   
   COPY train.py .
   COPY data/ data/
   
   CMD ["python", "train.py"]

Model serving container
~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: dockerfile

   FROM python:3.11-slim
   WORKDIR /app
   
   COPY requirements.txt .
   RUN pip install --no-cache-dir -r requirements.txt
   
   COPY model.pkl .
   COPY serve.py .
   
   EXPOSE 8000
   CMD ["uvicorn", "serve:app", "--host", "0.0.0.0", "--port", "8000"]

Jupyter notebook container
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: dockerfile

   FROM jupyter/scipy-notebook:latest
   
   COPY requirements.txt .
   RUN pip install --no-cache-dir -r requirements.txt
   
   EXPOSE 8888
   CMD ["jupyter", "lab", "--ip=0.0.0.0", "--allow-root"]

Debugging tips
--------------

Build with verbose output
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   docker build --progress=plain --no-cache -t my-image .

Inspect intermediate layers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   # Get layer IDs
   docker history my-image
   
   # Run shell in specific layer
   docker run -it <layer-id> /bin/bash

Check build context size
~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   # See what's being sent to Docker daemon
   docker build --no-cache -t test . 2>&1 | grep "Sending build context"

Next steps
----------

Now that you understand Dockerfiles, try the hands-on labs:

1. :doc:`lab-01-data-cleaner` - Basic Dockerfile
2. :doc:`lab-02-streamlit-app` - Web app with port mapping
3. :doc:`lab-03-ml-dev-container` - Dev container configuration
