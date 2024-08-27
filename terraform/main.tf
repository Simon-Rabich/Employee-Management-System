provider "helm" {
  # Ensure you have Helm provider configured
  # You can specify your Helm configuration here if needed
}

provider "kubernetes" {
  # Ensure you have Kubernetes provider configured
  # You can specify your Kubernetes configuration here if needed
}

resource "helm_release" "argocd" {
  name       = "argocd"
  repository = "https://argoproj.github.io/argo-helm"
  chart      = "argo-cd"
  version    = "5.2.9"  # Use the latest available version

  namespace = "argocd"

  set {
    name  = "server.extraArgs"
    value = "--insecure"
  }

  set {
    name  = "server.service.type"
    value = "LoadBalancer"
  }

  set {
    name  = "controller.replicas"
    value = "2"  # Adjust the number of replicas as needed
  }

  set {
    name  = "server.service.loadBalancerIP"
    value = ""  # Optional: specify a static IP if required
  }

  set {
    name  = "server.service.externalTrafficPolicy"
    value = "Cluster"  # Optional: use "Local" if you need local traffic policy
  }

  # Optional: if you have specific values to set
  # You can also specify a values file if you prefer
  # values = [file("values.yaml")]
}

resource "kubernetes_namespace" "argocd" {
  metadata {
    name = "argocd"
  }
}

