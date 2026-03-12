output "ecr_repository_name" {
  description = "Name of the ECR repository"
  value       = aws_ecr_repository.app_repo.name
}

output "ecr_repository_url" {
  description = "URL of the ECR repository"
  value       = aws_ecr_repository.app_repo.repository_url
}

output "ecs_cluster_name" {
  description = "Name of the ECS cluster"
  value       = aws_ecs_cluster.app_cluster.name
}

output "ecs_task_definition_family" {
  description = "ECS task definition family"
  value       = aws_ecs_task_definition.app_task.family
}

output "cloudwatch_log_group_name" {
  description = "CloudWatch log group for ECS task logs"
  value       = aws_cloudwatch_log_group.app_logs.name
}

output "ecs_service_name" {
  description = "Name of the ECS service"
  value       = aws_ecs_service.app_service.name
}

output "ecs_security_group_id" {
  description = "Security group ID for ECS service"
  value       = aws_security_group.ecs_service_sg.id
}
