output "backend_ecr_url" {
  value = aws_ecr_repository.backend_repo.repository_url
}

output "frontend_ecr_url" {
  value = aws_ecr_repository.frontend_repo.repository_url
}

output "ecs_cluster_name" {
  value = aws_ecs_cluster.main_cluster.name
}