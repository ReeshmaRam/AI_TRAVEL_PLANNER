## Parent image
FROM python:3.10-slim

## Essential environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

## Work directory inside the docker container ## this is used to create a docker container
WORKDIR /app

## Installing system dependancies
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

## Copying ur all contents from local to app ## pushing all the files to the docker container from local i.e github
COPY . .

## Run setup.py
RUN pip install --no-cache-dir -e . 
## no need to worry about cache files.

# Used PORTS 
## streamlit app runs on 8501 port
EXPOSE 8501

# Run the app 
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0", "--server.headless=true"]
