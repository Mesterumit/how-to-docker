# Use Python 3.11 slim image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install dependencies
RUN pip install --no-cache-dir \
    streamlit \
    pandas \
    plotly \
    psutil

# Copy application code
COPY app.py .

# Expose Streamlit's default port
EXPOSE 8501

# Set environment variable to prevent Streamlit from trying to open browser
ENV STREAMLIT_SERVER_HEADLESS=true

# Run Streamlit app
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
