output "frontend_ip" {
  value = aws_instance.frontend_server.public_ip
}

output "backend_ip" {
  value = aws_instance.backend_server.public_ip
}