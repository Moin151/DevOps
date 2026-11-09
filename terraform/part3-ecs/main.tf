provider "aws" {
  region = var.aws_region
}

resource "aws_ecr_repository" "backend_repo" {
  name = "devops-backend"
}

resource "aws_ecr_repository" "frontend_repo" {
  name = "devops-frontend"
}

resource "aws_ecs_cluster" "main_cluster" {
  name = "devops-ecs-cluster"
}