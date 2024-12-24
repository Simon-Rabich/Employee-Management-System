variable "namespace" {
  default     = "new-employee-app"
  description = "Kubernetes namespace for the app"
}

variable "app_name" {
  default     = "fastapi-app-new"
  description = "Name of the FastAPI app"
}

variable "image_repository" {
  default     = "simon658/fastapi-app"
  description = "Docker image repository for the app"
}

variable "image_tag" {
  default     = "latest"
  description = "Docker image tag for the app"
}

variable "service_type" {
  default     = "NodePort"
  description = "Type of Kubernetes service"
}

variable "service_node_port" {
  default     = 32000
  description = "NodePort for the Kubernetes service"
}

variable "db_user" {
  default     = "simonravitz"
  description = "Database username"
}

variable "db_pass" {
  default     = "Aa123456!"
  description = "Database password"
}
