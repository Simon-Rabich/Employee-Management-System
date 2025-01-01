provider "kubernetes" {
  config_path = "~/.kube/config" # Adjust if using a different kubeconfig
}

provider "helm" {
  kubernetes {
    config_path = "~/.kube/config"
  }
}

module "fastapi_app" {
  source            = "./modules/helm_release"
  helm_chart        = "../helm"            # Use the relative path to your Helm chart
  namespace         = var.namespace
  app_name          = var.app_name
  image_repository  = var.image_repository
  image_tag         = var.image_tag
  service_type      = var.service_type
  service_node_port = var.service_node_port
  db_user           = var.db_user
  db_pass           = var.db_pass
}
