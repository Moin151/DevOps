#!/bin/bash
apt-get update -y
apt-get install -y python3-pip python3-venv nodejs npm git

cd /home/ubuntu
git clone https://github.com/Moin151/DevOps.git
cd DevOps

# Setup Backend (Flask)
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
export MONGO_URI="mongodb+srv://dummy:1234@cluster0.qqeazm5.mongodb.net/tutedude_db?retryWrites=true&w=majority"
nohup python3 app.py > flask.log 2>&1 &
deactivate

# Setup Frontend (Express)
cd ../frontend
npm install
export FLASK_URL="http://localhost:5000"
nohup npm start > express.log 2>&1 &