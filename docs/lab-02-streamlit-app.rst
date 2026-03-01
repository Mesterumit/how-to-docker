Lab 2: Streamlit dashboard container
=====================================

.. note::
   
   📁 `View lab files on GitHub <https://github.com/gperdrizet/how-to-docker/tree/main/02-streamlit-app>`_

Learning objectives
-------------------

- Containerize a web application (Streamlit)
- Understand port mapping to access containerized apps
- Use volumes to share data between host and container
- Work with containers in detached mode
- See how containers make applications instantly portable

What's included
---------------

- ``app.py``: An interactive Streamlit dashboard for data visualization
- ``Dockerfile``: Instructions to build the containerized app
- ``.dockerignore``: Files to exclude from the build

The scenario
------------

You've built an interactive data dashboard for your team. By containerizing it:

- Team members can run it without installing Streamlit, pandas, or plotly
- The app works identically on macOS, Windows, and Linux
- You can deploy and scale it on any cloud platform
- Multiple versions can run simultaneously on different ports
- It can easily be updated and/or changed independently of other components

Step-by-step instructions
--------------------------

1. Examine the Dockerfile
~~~~~~~~~~~~~~~~~~~~~~~~~~

Navigate to the example directory:

.. code-block:: bash

   cd 02-streamlit-app

Notice new elements compared to Lab 1:

.. code-block:: dockerfile

   FROM python:3.11-slim
   WORKDIR /app
   RUN pip install streamlit pandas plotly  # Multiple packages
   COPY app.py .
   EXPOSE 8501                              # Document the port
   ENV STREAMLIT_SERVER_HEADLESS=true       # Environment variable
   CMD ["streamlit", "run", "app.py", ...]  # Run web server

**New concepts**:

- ``EXPOSE 8501``: Documents that the container listens on port 8501 (Streamlit's default)
- ``ENV``: Sets environment variables (tells Streamlit not to open a browser)
- Multiple packages installed in one ``RUN`` command (faster build)

2. Build the image
~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   docker build -t streamlit-dashboard .

This might take a minute as it installs Streamlit and dependencies.

3. Run the container with port mapping
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   docker run --rm -p 8501:8501 streamlit-dashboard

**What's happening**:

- ``-p 8501:8501``: Maps port 8501 on your computer to port 8501 in the container
- Format is ``-p HOST_PORT:CONTAINER_PORT``
- Now you can access the containerized app via localhost

4. Access the dashboard
~~~~~~~~~~~~~~~~~~~~~~~

Open your browser and navigate to:

.. code-block:: text

   http://localhost:8501

You should see the Data Insights Dashboard running!

The app is running completely inside a container but accessible through your browser.

5. Explore the dashboard
~~~~~~~~~~~~~~~~~~~~~~~~

Try these features:

- View the sample dataset
- Check statistical summaries
- Create distribution plots
- Compare numeric columns
- View correlation heatmap
- Filter data with the slider

6. Load your own data (optional)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can upload a CSV file using the sidebar uploader, or mount data from your host system.

To mount external data, stop the container (``Ctrl+C``) and restart with a volume:

.. tab-set::

   .. tab-item:: Linux/macOS

      .. code-block:: bash

         docker run --rm -p 8501:8501 \
           -v /path/to/your/data:/data \
           streamlit-dashboard

   .. tab-item:: Windows PowerShell

      .. code-block:: powershell

         docker run --rm -p 8501:8501 `
           -v C:/path/to/your/data:/data `
           streamlit-dashboard

   .. tab-item:: Windows CMD

      .. code-block:: batch

         docker run --rm -p 8501:8501 ^
           -v C:\path\to\your\data:/data ^
           streamlit-dashboard

Note: On Windows, use forward slashes in the container path and include the drive letter in the host path.

Then modify the app to read from ``/data/your-file.csv``.

7. Run on a different port
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Stop the container (``Ctrl+C``) and try running on a different port:

.. code-block:: bash

   docker run --rm -p 8080:8501 streamlit-dashboard

Now access it at ``http://localhost:8080``. Notice:

- Container still uses port 8501 internally
- Host port 8080 maps to container port 8501
- Multiple instances can run on different host ports

8. Run in detached mode
~~~~~~~~~~~~~~~~~~~~~~~~

Run the container in the background:

.. code-block:: bash

   docker run --rm -d -p 8501:8501 --name my-dashboard streamlit-dashboard

**New flags**:

- ``-d``: Detached mode (runs in background)
- ``--name my-dashboard``: Give the container a friendly name

Access the dashboard at ``http://localhost:8501``, then check it's running:

.. code-block:: bash

   docker ps

View logs:

.. code-block:: bash

   docker logs my-dashboard

Follow logs in real-time:

.. code-block:: bash

   docker logs -f my-dashboard

Stop it when done:

.. code-block:: bash

   docker stop my-dashboard

Key concepts
------------

- **Port mapping**: Exposing containerized applications to your host machine
- **Web application containers**: Running interactive apps in isolation
- **Environment variables**: Configuring containers at runtime
- **Detached mode**: Running containers in the background
- **Container naming**: Managing multiple containers easily

Use cases for ML/data science
------------------------------

This pattern is perfect for:

- **Model demos**: Quickly share model predictions with stakeholders
- **Data exploration**: Distribute analysis dashboards to your team
- **ML model monitoring**: Build dashboards showing model performance
- **Experiment tracking**: Visualize training metrics
- **Data validation**: Interactive tools for checking data quality

Experiment further
------------------

1. **Modify the dashboard**: Edit ``app.py`` to add new visualizations
2. **Rebuild and see changes**: Rebuild the image and restart the container
3. **Link to example 1**: Mount the cleaned data from the first example
4. **Multiple instances**: Run the same container on ports 8501, 8502, 8503 simultaneously

What's next?
------------

In :doc:`lab-03-ml-dev-container`, you'll build a complete development environment container, customize it for ML work, publish it to Docker Hub, and launch it in GitHub Codespaces!

---

**Common issues**:

- **Port already in use**: Change the host port: ``-p 8502:8501``
- **Browser doesn't load**: Wait 5-10 seconds for Streamlit to start, check ``docker logs``
- **Container exits immediately**: Check logs with ``docker logs <container-id>``
