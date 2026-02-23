Overview
========

This tutorial provides a hands-on introduction to Docker containerization specifically designed for AI/ML bootcamp students transitioning from Jupyter notebooks to production-ready applications.

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

What You'll Build
-----------------

Through three progressive examples, you'll:

1. **Data Cleaner** (3 min): A containerized pandas-based data processing component demonstrating modular ML pipelines
2. **Streamlit Dashboard** (5 min): An interactive web app showing port mapping and container networking
3. **ML Dev Container** (10 min): Your own customized, publishable development environment for course projects

**Total time**: 30-45 minutes

Prerequisites
-------------

Before starting, ensure you have:

- **Docker Desktop** installed (`Get Docker <https://www.docker.com/products/docker-desktop/>`_)
- **Docker Hub account** (`Sign up <https://hub.docker.com/signup>`_)
- **VS Code** with Remote-Containers extension (optional but recommended)
- **GitHub account** (for Codespaces verification)
- Basic Python and command line knowledge

Ready to Start?
---------------

Head to :doc:`Docker Concepts </introduction/concepts>` to understand the fundamentals, or jump straight to :doc:`Example 1 </examples/01-data-cleaner>` if you're already familiar with Docker basics.
