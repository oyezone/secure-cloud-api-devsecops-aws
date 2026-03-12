variable "aws_region" {
  description = "AWS region for deployment"
  type        = string
  default     = "us-east-1"
}

variable "project_name" {
  description = "Project name prefix"
  type        = string
  default     = "connected-vehicle-api"
}

variable "environment" {
  description = "Deployment environment"
  type        = string
  default     = "dev"
}

variable "container_port" {
  description = "Container port for the application"
  type        = number
  default     = 8000
}

variable "aws_account_id" {
  description = "AWS account ID"
  type        = string
  default     = "902883117782"
}
