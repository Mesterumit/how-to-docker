Lab 1: Data cleaner container
==============================

.. note::
   
   📁 `View lab files on GitHub <https://github.com/gperdrizet/how-to-docker/tree/main/01-data-cleaner>`_

Learning objectives
-------------------

- Understand the basic structure of a Dockerfile
- Build your first Docker image
- Run a containerized Python application
- Use volume mounts to share data between host and container
- See how containers enable modular ML pipeline components

What's included
---------------

- ``clean_data.py``: A pandas-based data cleaning script
- ``Dockerfile``: Instructions to build the container image
- ``sample_data.csv``: Sample dataset with duplicates and missing values
- ``.dockerignore``: Files to exclude from the Docker build context

The scenario
------------

Imagine you're building a production ML pipeline. The data cleaning step is containerized as a separate component that can:

- Run independently of other pipeline stages
- Scale horizontally to process multiple datasets in parallel
- Be updated without affecting training or serving containers
- Run consistently across development, staging, and production environments

Step-by-step instructions
--------------------------

1. Examine the Dockerfile
~~~~~~~~~~~~~~~~~~~~~~~~~

Navigate to the example directory and open the Dockerfile:

.. code-block:: bash

   cd 01-data-cleaner

Notice the structure:

.. code-block:: dockerfile

   FROM python:3.11-slim            # Start with Python base image
   WORKDIR /app                     # Set working directory
   RUN pip install pandas           # Install dependencies
   COPY clean_data.py .             # Copy our script
   CMD ["python", "clean_data.py"]  # Default command

Each instruction creates a layer in the image. Docker caches layers, so rebuilds are fast when only later layers change.

2. Build the Docker image
~~~~~~~~~~~~~~~~~~~~~~~~~~

From the ``01-data-cleaner`` directory, run:

.. code-block:: bash

   docker build -t data-cleaner .

**What's happening**:

- ``-t data-cleaner``: Tags the image with the name "data-cleaner"
- ``.``: Build context is the current directory

Watch Docker execute each Dockerfile instruction and create layers.

3. Verify the image
~~~~~~~~~~~~~~~~~~~~

List your Docker images:

.. code-block:: bash

   docker images | grep data-cleaner

You should see your newly created image with its size and creation time.

4. Prepare data directory
~~~~~~~~~~~~~~~~~~~~~~~~~~

Create directories for input and output:

.. tab-set::

   .. tab-item:: Linux/macOS

      .. code-block:: bash

         mkdir -p data/input data/output
         cp sample_data.csv data/input/raw_data.csv

   .. tab-item:: Windows PowerShell

      .. code-block:: powershell

         mkdir -p data/input, data/output
         cp sample_data.csv data/input/raw_data.csv

   .. tab-item:: Windows CMD

      .. code-block:: batch

         mkdir data\input data\output
         copy sample_data.csv data\input\raw_data.csv

5. Run the container
~~~~~~~~~~~~~~~~~~~~

.. tab-set::

   .. tab-item:: Linux/macOS

      .. code-block:: bash

         docker run --rm -v "$(pwd)/data:/data" data-cleaner

   .. tab-item:: Windows PowerShell

      .. code-block:: powershell

         docker run --rm -v "${PWD}/data:/data" data-cleaner

   .. tab-item:: Windows CMD

      .. code-block:: batch

         docker run --rm -v "%cd%/data:/data" data-cleaner

**What's happening**:

- ``--rm``: Automatically remove the container when it exits
- ``-v``: Mount your local ``data/`` directory to ``/data`` in the container (syntax varies by OS/shell)
- ``data-cleaner``: The image to run

6. Examine the output
~~~~~~~~~~~~~~~~~~~~~~

The script displays:

- Original dataset statistics
- Missing values found
- Cleaning operations performed
- Cleaned dataset summary

Check the cleaned file:

.. tab-set::

   .. tab-item:: Linux/macOS

      .. code-block:: bash

         cat data/output/cleaned_data.csv

   .. tab-item:: Windows

      .. code-block:: batch

         type data\output\cleaned_data.csv

Notice:

- Duplicates removed (Alice and Bob appeared twice)
- Rows with missing values removed (David had no age, Eve had no score)
- Whitespace trimmed (Frank's city "  Austin  " became "Austin")

Key concepts reinforced
-----------------------

- **Dockerfile basics**: FROM, WORKDIR, RUN, COPY, CMD
- **Image building**: Creating reusable templates for containers
- **Volume mounts**: Sharing data between host and container
- **Container isolation**: The script runs in its own environment with only pandas installed
- **Modularity**: This component could be part of a larger pipeline, processing data before training

Experiment further
------------------

Try these modifications:

1. **Change the cleaning logic**: Edit ``clean_data.py`` to fill missing values instead of dropping them
2. **Rebuild and rerun**: Notice Docker's layer caching makes rebuilds fast
3. **Process different data**: Replace ``sample_data.csv`` with your own CSV file
4. **Check container cleanup**: Run ``docker ps -a`` to verify ``--rm`` removed the container

What's next?
------------

In :doc:`lab-02-streamlit-app`, you'll containerize an interactive web application and learn about port mapping to access apps running inside containers.

---

**Troubleshooting**: If you're stuck, check that:

- Docker Desktop is running
- You're in the ``01-data-cleaner/`` directory
- The data directories were created correctly
