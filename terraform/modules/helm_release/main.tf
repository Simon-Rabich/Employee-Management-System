resource "helm_release" "fastapi_app" {
  name       = var.app_name
  repository = ""              # Leave empty for local charts
  chart      = var.helm_chart  # Path to the local Helm chart
  namespace  = var.namespace

  set {
    name  = "image.repository"
    value = var.image_repository
  }

  set {
    name  = "image.tag"
    value = var.image_tag
  }

  set {
    name  = "service.type"
    value = var.service_type
  }

  set {
    name  = "service.nodePort"
    value = var.service_node_port
  }

  set {
  name  = "env.DATABASE_URL"
  value = "postgresql://${var.db_user}:${var.db_pass}@${var.app_name}-new-employee-app-postgres:5432/crmdb"
}

}
