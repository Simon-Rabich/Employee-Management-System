variable "helm_chart" {
  description = "Path to the Helm chart"
}

variable "namespace" {
  description = "Kubernetes namespace"
}
variable "app_name" {
  description = "The name of the application"
  type        = string
}

variable "image_repository" {
  description = "Docker image repository"
}

variable "image_tag" {
  description = "Docker image tag"
}

variable "service_type" {
  description = "Service type for Kubernetes"
}

variable "service_node_port" {
  description = "NodePort for the Kubernetes service"
}

variable "db_user" {
  description = "PostgreSQL database user"
  type        = string
}

variable "db_pass" {
  description = "PostgreSQL database password"
  type        = string
}



