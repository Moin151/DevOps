### Cross-Instance Networking & Security Group Rules (Task 2)
When deploying the Express frontend and Flask backend on **separate EC2 instances**, security groups enforce strict isolation:
1. **Frontend EC2 Security Group**:
   - Inbound: Allow port `3000` (HTTP) from `0.0.0.0/0` (Public client access).
   - Outbound: Allow all traffic.
2. **Backend EC2 Security Group**:
   - Inbound: Allow port `5000` (Flask API) **only** from the Private IP or Security Group ID of the Frontend EC2 instance (preventing unauthorized public access).
   - Outbound: Allow all traffic.
3. **Environment Configuration**: The frontend instance communicates with the backend via an environment variable pointing to the backend's internal IP: `FLASK_URL=http://<BACKEND_PRIVATE_IP>:5000`.