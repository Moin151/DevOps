output "instance_public_ip" {
  value       = aws_instance.app_server.public_ip
  description = "Public IP address of the single EC2 instance"
}

output "frontend_url" {
  value       = "http://${aws_instance.app_server.public_ip}:3000"
  description = "URL to access the Express frontend"
}