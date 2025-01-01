resource "kubernetes_secret" "postgres_secret" {
  metadata {
    name      = "postgres-secret"
    namespace = var.namespace
  }

  data = {
    username = var.db_user
    password = var.db_pass
  }
}
