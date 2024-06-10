import subprocess

# Check Docker version
# docker --version
subprocess.run(["docker", "--version"])

# Pull an image from Docker Hub
# docker pull python:3.8-slim
subprocess.run(["docker", "pull", "python:3.8-slim"])

# Run a container from an image
# docker run -d --name my-python-app python:3.8-slim
subprocess.run(["docker", "run", "-d", "--name", "my-python-app", "python:3.8-slim"])

# List running containers
# docker ps
subprocess.run(["docker", "ps"])

# List all containers (running and stopped)
# docker ps -a
subprocess.run(["docker", "ps", "-a"])

# Stop a running container
# docker stop my-python-app
subprocess.run(["docker", "stop", "my-python-app"])

# Remove a stopped container
# docker rm my-python-app
subprocess.run(["docker", "rm", "my-python-app"])

# Remove an image
# docker rmi python:3.8-slim
subprocess.run(["docker", "rmi", "python:3.8-slim"])

# Build an image from a Dockerfile
# docker build -t my-python-app .
subprocess.run(["docker", "build", "-t", "my-python-app", "."])

# Start containers using Docker Compose
# docker-compose up
subprocess.run(["docker-compose", "up"])

# Stop and remove containers, networks, images, and volumes defined in a docker-compose.yml file
# docker-compose down
subprocess.run(["docker-compose", "down"])

#Docker Image
# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variable
ENV NAME World

# Run app.py when the container launches
CMD ["python", "app.py"]


#yaml FIle
import yaml

data = {
    'version': '3',
    'services': {
        'web': {
            'image': 'nginx',
            'ports': ['80:80']
        },
        'db': {
            'image': 'postgres',
            'environment': {
                'POSTGRES_PASSWORD': 'example'
            }
        }
    }
}

with open("output-compose.yml", 'w') as file:
    yaml.dump(data, file, default_flow_style=False)
