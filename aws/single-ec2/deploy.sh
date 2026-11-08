#!/bin/bash
<<<<<<< HEAD
# Exit immediately if a command exits with a non-zero status
set -e

echo "Updating system packages..."
sudo apt-get update -y
sudo apt-get install -y docker.io docker-compose git

echo "Starting Docker service..."
=======
set -e

echo "=== Starting Single EC2 Deployment ==="

# Update system and install Docker & Docker Compose
sudo apt-get update -y
sudo apt-get install -y docker.io docker-compose git

# Start and enable Docker
>>>>>>> a7c09ad (Update frontend configuration for separate EC2 backend IP)
sudo systemctl start docker
sudo systemctl enable docker
sudo usermod -aG docker $USER

<<<<<<< HEAD
echo "Cloning or setting up application repository..."
# Assuming code is already present or cloned here
cd /home/ubuntu/DevOps || cd /workspaces/DevOps

echo "Building and launching containers via Docker Compose..."
sudo docker-compose up -d --build

echo "Deployment complete! Application running on port 3000."
=======
echo "=== Docker Installed Successfully ==="

# Check if docker-compose.yml exists in the working directory
if [ -f "docker-compose.yml" ]; then
    echo "Building and starting containers..."
    sudo docker-compose up -d --build
    echo "Deployment complete! App is running."
else
    echo "Error: docker-compose.yml not found in the current directory."
    exit 1
fi
>>>>>>> a7c09ad (Update frontend configuration for separate EC2 backend IP)
