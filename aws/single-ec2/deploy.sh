#!/bin/bash
# Exit immediately if a command exits with a non-zero status
set -e

echo "Updating system packages..."
sudo apt-get update -y
sudo apt-get install -y docker.io docker-compose git

echo "Starting Docker service..."
sudo systemctl start docker
sudo systemctl enable docker
sudo usermod -aG docker $USER

echo "Cloning or setting up application repository..."
# Assuming code is already present or cloned here
cd /home/ubuntu/DevOps || cd /workspaces/DevOps

echo "Building and launching containers via Docker Compose..."
sudo docker-compose up -d --build

echo "Deployment complete! Application running on port 3000."