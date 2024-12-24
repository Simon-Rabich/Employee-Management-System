output "service_url" {
  value = "http://<node-ip>:${var.service_node_port}"
  description = "URL to access the FastAPI service"
}
