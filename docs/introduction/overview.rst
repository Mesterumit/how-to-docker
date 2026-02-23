Overview
========

This tutorial provides a hands-on introduction to Docker containerization specifically designed for AI/ML bootcamp students transitioning from Jupyter notebooks to production-ready applications.

Duration
--------

**30-45 minutes** total:

- 5 min: Introduction and prerequisites
- 5 min: Docker concepts overview
- 3 min: Example 1 - Data cleaner
- 5 min: Example 2 - Streamlit app
- 10 min: Example 3 - Dev container (hands-on)
- 5 min: Publishing to Docker Hub
- 5 min: Codespaces verification
- 2-7 min: Q&A and next steps

Learning Objectives
-------------------

By the end of this tutorial, you will be able to:

✅ Understand why containerization matters for ML engineering

✅ Build Docker images from Dockerfiles

✅ Run containerized applications with volume mounts and port mapping

✅ Create a VS Code development container for ML projects

✅ Publish container images to Docker Hub

✅ Launch your environment in GitHub Codespaces

Who This Is For
---------------

This tutorial is designed for:

- **AI/ML bootcamp students** ready to move beyond notebooks
- **Data scientists** wanting to productionize their workflows
- **ML engineers** new to containerization
- **Anyone** interested in reproducible ML development environments

What You'll Build
-----------------

Through three progressive examples, you'll:

1. **Data Cleaner**: A containerized pandas-based data processing component demonstrating modular ML pipelines
2. **Streamlit Dashboard**: An interactive web app showing port mapping and container networking
3. **ML Dev Container**: Your own customized, publishable development environment for course projects

Prerequisites Check
--------------------

Make sure you have:

.. code-block:: bash

   # Check Docker is installed
   docker --version
   
   # Check Docker is running
   docker ps

If Docker isn't installed, visit the :doc:`installation guide </introduction/installation>`.

Ready to Start?
---------------

Head to :doc:`Docker Concepts </introduction/concepts>` to understand the fundamentals, or jump straight to :doc:`Example 1 </examples/01-data-cleaner>` if you're already familiar with Docker basics.
