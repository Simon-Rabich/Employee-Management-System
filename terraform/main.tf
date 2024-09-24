# main.tf

provider "kubernetes" {
  config_path = "~/.kube/config"
}

provider "helm" {
  kubernetes {
    config_path = "~/.kube/config"
  }
}

resource "helm_release" "fastapi_app" {
  name       = "fastapi-app"
  repository = "https://charts.helm.sh/stable"
  chart      = "path-to-your-chart"
  namespace  = "new-employee-app"

  set {
    name  = "image.repository"
    value = "simon658/fastapi-app"
  }

  set {
    name  = "image.tag"
    value = "latest"
  }

  set {
    name  = "service.type"
    value = "NodePort"
  }

  set {
    name  = "service.nodePort"
    value = "32000"
  }

  set {
    name  = "env.DATABASE_URL"
    value = "postgresql://$(DB_USER):$(DB_PASS)@fastapi-app-new-employee-app-postgres:5432/crmdb"
  }

  set_sensitive {
    name  = "extraEnv.DB_USER"
    value = "simonravitz"
  }

  set_sensitive {
    name  = "extraEnv.DB_PASS"
    value = "Aa123456!"
  }
}

resource "kubernetes_secret" "postgres_secret" {
  metadata {
    name      = "postgres-secret"
    namespace = "new-employee-app"
  }

  data = {
    username = "simonravitz"
    password = "your_password"
  }
}
