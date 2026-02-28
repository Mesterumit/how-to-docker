# Example 1: Data cleaner container

**Time to complete**: ~3 minutes

## Learning objectives

- Understand the basic structure of a Dockerfile
- Build your first Docker image
- Run a containerized Python application
- Use volume mounts to share data between host and container
- See how containers enable modular ML pipeline components

## What's included

- `clean_data.py`: A pandas-based data cleaning script
- `Dockerfile`: Instructions to build the container image
- `sample_data.csv`: Sample dataset with duplicates and missing values
- `.dockerignore`: Files to exclude from the Docker build context

## The scenario

Imagine you're building a production ML pipeline. The data cleaning step is containerized as a separate component that can:
- Run independently of other pipeline stages
- Scale horizontally to process multiple datasets in parallel
- Be updated without affecting training or serving containers
- Run consistently across development, staging, and production environments

## Step-by-step instructions

### 1. Examine the Dockerfile

Open `Dockerfile` and notice the structure:

```dockerfile
FROM python:3.11-slim            # Start with Python base image
WORKDIR /app                     # Set working directory
RUN pip install pandas           # Install dependencies
COPY clean_data.py .             # Copy our script
CMD ["python", "clean_data.py"]  # Default command
```

Each instruction creates a layer in the image. Docker caches layers, so rebuilds are fast when only later layers change.

### 2. Build the Docker Image

From this directory, run:

```bash
docker build -t data-cleaner .
```

**What's happening**:
- `-t data-cleaner`: Tags the image with the name "data-cleaner"
- `.`: Build context is the current directory

Watch Docker execute each Dockerfile instruction and create layers.

### 3. Verify the Image

List your Docker images:

```bash
docker images | grep data-cleaner
```

You should see your newly created image with its size and creation time.

### 4. Prepare Data Directory

Create directories for input and output:

```bash
mkdir -p data/input data/output
cp sample_data.csv data/input/raw_data.csv
```

### 5. Run the Container

```bash
docker run --rm -v "$(pwd)/data:/data" data-cleaner
```

**What's happening**:
- `--rm`: Automatically remove the container when it exits
- `-v "$(pwd)/data:/data"`: Mount your local `data/` directory to `/data` in the container
- `data-cleaner`: The image to run

### 6. Examine the Output

The script displays:
- Original dataset statistics
- Missing values found
- Cleaning operations performed
- Cleaned dataset summary

Check the cleaned file:

```bash
cat data/output/cleaned_data.csv
```

Notice:
- Duplicates removed (Alice and Bob appeared twice)
- Rows with missing values removed (David had no age, Eve had no score)
- Whitespace trimmed (Frank's city "  Austin  " became "Austin")

## Key concepts reinforced

- **Dockerfile basics**: FROM, WORKDIR, RUN, COPY, CMD
- **Image building**: Creating reusable templates for containers
- **Volume mounts**: Sharing data between host and container
- **Container isolation**: The script runs in its own environment with only pandas installed
- **Modularity**: This component could be part of a larger pipeline, processing data before training

## Experiment further

Try these modifications:

1. **Change the cleaning logic**: Edit `clean_data.py` to fill missing values instead of dropping them
2. **Rebuild and rerun**: Notice Docker's layer caching makes rebuilds fast
3. **Process different data**: Replace `sample_data.csv` with your own CSV file
4. **Check container cleanup**: Run `docker ps -a` to verify `--rm` removed the container

## What's next?

In [02-streamlit-app](../02-streamlit-app/), you'll containerize an interactive web application and learn about port mapping to access apps running inside containers.

---

**Time check**: You should complete this example in about 3 minutes. If you're stuck, check that:
- Docker Desktop is running
- You're in the `01-data-cleaner/` directory
- The data directories were created correctly
