# DevOps Multi-Tier Deployment Project

This repository contains a full-stack web application consisting of a **Flask Backend (Python)**, an **Express Frontend (Node.js)**, and a persistent **MongoDB Atlas** database. 

The project demonstrates three progressive cloud deployment configurations on **Amazon Web Services (AWS)** as part of the DevOps architecture assignment.

---

## 🏗️ Project Architecture
- **Frontend**: Node.js & Express (Runs on port `3000`, renders UI and handles client requests).
- **Backend**: Python & Flask (Runs on port `5000`, processes API logic and connects to database).
- **Database**: MongoDB Atlas cloud cluster (`tutedude_db`).

---

## 🚀 Deployment Configurations

### Phase 1: Single Amazon EC2 Instance
In this configuration, both the Flask backend and the Express frontend run concurrently on a single Ubuntu EC2 instance.
* **Automation Script**: Located at `aws/single-ec2/deploy.sh`.
* **What it does**: Updates system packages, installs Python, Node.js, and Git, sets up virtual environments, configures environment variables (`MONGO_URI` and `FLASK_URL`), and launches both services in the background using `nohup`.
* **Access**: `http://<your-ec2-public-ip>:3000`

### Phase 2: Separate EC2 Instances (Multi-Tier Architecture)
In this setup, the application tiers are decoupled across two independent virtual machines to mimic production isolation:
1. **Instance 1 (Backend Server)**: Hosts the Flask API and connects securely to MongoDB Atlas. Security groups allow inbound traffic on port `5000`.
2. **Instance 2 (Frontend Server)**: Hosts the Express Node application. Configured with the backend's private/public IP via the `FLASK_URL` environment variable. Security groups expose port `3000` to users.

### Phase 3: Containerized Deployment via AWS ECR, ECS & VPC
This phase utilizes container orchestration via **AWS Fargate** (Serverless containers):
1. **Amazon ECR**: Custom Docker images for both backend (`flask-backend`) and frontend (`express-frontend`) are stored in private ECR repositories.
2. **Amazon VPC**: Configured with public subnets and internet gateways to allow outbound container communication with MongoDB Atlas.
3. **Amazon ECS**: Task definitions and services orchestrate the containers, managing scaling and network routing between the frontend and backend services.

---

## 🛑 Cost Management Notice
To avoid incurring unwanted charges on the AWS Free Tier, all running EC2 instances and ECS services are kept **stopped or terminated** when not actively being evaluated or tested.