Docker for AI/ML Bootcamp
==========================

A hands-on introduction to containerization for machine learning and data science workflows.

Welcome to the Docker tutorial designed for AI/ML bootcamp students. This 30-45 minute introduction teaches containerization fundamentals through three progressive hands-on examples, culminating in creating and publishing your own ML development environment.

.. image:: _static/docker-ml-banner.svg
   :alt: Docker for ML
   :align: center
   :width: 600px

What You'll Learn
-----------------

1. **Docker Basics**: Images, containers, Dockerfiles, and key concepts
2. **Building Containers**: From simple scripts to web applications
3. **Development Containers**: Creating portable, shareable ML development environments
4. **Publishing Images**: Sharing your work via Docker Hub
5. **Portability**: Verifying your environment works anywhere (GitHub Codespaces)

Why Containerization for ML?
-----------------------------

In production machine learning systems, containerization is essential for building reliable, scalable, and reproducible pipelines.

.. mermaid::

   graph TB
       subgraph "Production ML System"
           A[Data Ingestion Container] --> B[Data Cleaning Container]
           B --> C[Feature Store Container]
           C --> D[Training Container]
           D --> E[Model Registry Container]
           E --> F[Model Serving API Container]
           F --> G[API Gateway Container]
           
           H[(Data Lake)] -.-> A
           I[(Database)] -.-> C
           E -.-> J[Monitoring & Logging Container]
           F -.-> J
       end
       
       K[Client Applications] --> G
       G --> F

**Key Benefits:**

- **Reproducibility**: Exact dependencies across all environments
- **Modularity**: Independent scaling and updates of components
- **Portability**: Run anywhere without "works on my machine" problems
- **Isolation**: Multiple models with conflicting dependencies side-by-side
- **Collaboration**: Share entire development environments via images

Quick Start
-----------

Choose an example to begin:

.. grid:: 1 2 2 3
   :gutter: 3

   .. grid-item-card:: 📦 Data Cleaner
      :link: examples/01-data-cleaner
      :link-type: doc

      3 minutes
      ^^^
      Build a containerized data processing pipeline component.

   .. grid-item-card:: 📊 Streamlit App
      :link: examples/02-streamlit-app
      :link-type: doc

      5 minutes
      ^^^
      Run an interactive dashboard in a container.

   .. grid-item-card:: 🚀 Dev Container
      :link: examples/03-ml-dev-container
      :link-type: doc

      10 minutes
      ^^^
      Create, customize, and publish your ML dev environment.

Prerequisites
-------------

Before starting, ensure you have:

- **Docker Desktop** installed (`Get Docker <https://www.docker.com/products/docker-desktop/>`_)
- **Docker Hub account** (`Sign up <https://hub.docker.com/signup>`_)
- **VS Code** with Remote-Containers extension (optional but recommended)
- **GitHub account** (for Codespaces verification)
- Basic Python and command line knowledge

.. toctree::
   :maxdepth: 2
   :caption: Getting Started

   introduction/overview
   introduction/concepts
   introduction/dockerfile-guide

.. toctree::
   :maxdepth: 2
   :caption: Hands-On Examples

   examples/01-data-cleaner
   examples/02-streamlit-app
   examples/03-ml-dev-container

.. toctree::
   :maxdepth: 2
   :caption: Guides

   guides/dev-containers
   guides/publishing-images
   guides/codespaces

.. toctree::
   :maxdepth: 2
   :caption: Resources

   resources/troubleshooting
   resources/next-steps
   resources/faq

Indices and tables
==================

* :ref:`genindex`
* :ref:`search`
