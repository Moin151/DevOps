# Single EC2 Deployment Guide

## Architecture
- **Frontend**: Node.js & Express running on port `3000`
- **Backend**: Python & Flask running on port `5000`
- **Database**: MongoDB Atlas Cloud Cluster

## Steps to Deploy on AWS EC2
1. Launch an Ubuntu 22.04 LTS instance (`t2.micro` free tier).
2. Configure Security Group inbound rules to allow:
   - Port `22` (SSH)
   - Port `3000` (Express Frontend)
   - Port `5000` (Flask Backend)
3. SSH into your instance using your `.pem` key:
   ```bash
   chmod 400 your-key.pem
   ssh -i "your-key.pem" ubuntu@your-ec2-public-ip