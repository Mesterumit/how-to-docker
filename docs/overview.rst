Overview
========

This tutorial provides a hands-on introduction to Docker containerization for AI/ML.

Topics
------

1. **Docker basics**: Images, containers, Dockerfiles, and key concepts
2. **Building containers**: From simple scripts to web applications
3. **Development containers**: Creating portable, shareable ML development environments
4. **Publishing images**: Sharing your work via Docker Hub
5. **Portability**: Verifying your environment works anywhere (GitHub Codespaces)

Why containerization for ML?
-----------------------------

In production machine learning systems, containerization simplifies building reliable, scalable, and reproducible pipelines.

.. mermaid::

   %%{init: {'theme':'base', 'themeVariables': { 'primaryColor':'#e3f2fd','primaryTextColor':'#000000','primaryBorderColor':'#000000','lineColor':'#000000','secondaryColor':'#fff3e0','tertiaryColor':'#f1f8e9','fontSize':'26px'}}}%%
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

What you'll build
-----------------

Through three progressive examples, you'll:

1. **Data Cleaner** (3 min): A containerized pandas-based data processing component demonstrating modular ML pipeline components
2. **Streamlit Dashboard** (5 min): An interactive web app showing port mapping and container networking
3. **ML Dev Container** (10 min): Your own customized, publishable development environment for course projects

**Total time**: 30-45 minutes

Prerequisites
-------------

Before starting, ensure you have:

- **Docker** installed (`Get Docker <https://www.docker.com/products/docker-desktop/>`_)
- **Docker Hub account** (`Sign up <https://hub.docker.com/signup>`_)
- **VS Code** with Remote-Containers extension (optional but recommended)
- **GitHub account** (for Codespaces verification)
- Basic Python and command line knowledge

Ready to start?
---------------

Head to :doc:`concepts` to understand the fundamentals, or jump straight to :doc:`example-01-data-cleaner` if you're already familiar with Docker basics.
