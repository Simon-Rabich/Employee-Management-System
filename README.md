# 🚀 Employee Management System

A FastAPI-based Employee Management System with DevOps integrations.

## CLI Program Demonstrate CRUD action
```bash
python main.py
```
## Data Base using PostgresSQL
```bash
psql -U simonravitz -h localhost postgres
```
## FastAPI - using Uvicorn, which is an ASGI (Asynchronous Server Gateway Interface) server. + openapi
```bash
uvicorn src.main:app --host 0.0.0.0 --port 8000
```
## docker-compose - setting up locally
```bash
docker-compose up --build
```
## Kubernetes
```bash
minikube start
```
## Start Kubernetes
```bash
minikube start
```
## Run Kubernetes
```bash
kubectl port-forward deployment/employee-management-system 8080:8000
```
## GitOps using ArgoCD
```bash
kubectl port-forward svc/argocd-server -n argocd 8081:443
```
## Get ArgoCD Password for UI 
```bash
 argocd admin initial-password -n argocd
```
## Start Nexus - Artifact Register Repository
```bash
/usr/local/nexus/bin/nexus start
```


## Deploy or Upgrade with Helm Chart
```bash
helm upgrade --install employee-management-system ./helm-employee-management-system
```
## Check Helm Deploy
```bash
 helm status employee-management-system
```
## Logs
```bash
 helm install employee-management-system ./helm-employee-management-system --debug --dry-run
```
## Verify the Deployment
```bash
 kubectl get pvc
```
```bash
 kubectl get pods
```
```bash
 kubectl get svc
```

## 📦 Installation
```bash
pip install employee_management_system
```

## 🛠️ Tools

**Helm**
**Nexus**
**K8S**
**ArgoCD**

🔄 **Alembic**: DB Migration

🔗 **SQLAlchemy**: ORM

🐘 **Postgres**: DB

⚡  **FastAPI**: REST API Framework

📄 **Swagger OpenAPI**: Interactive UI API Docs

🔧 **GitHub Actions**: CI

🐳 **Docker Compose**: Rapid Setup & Containerization

🐳 **Dockerfile**: Rapid Setup & Containerization

🚀 **Uvicorn**: ASGI Web Server

🔐 **Pydantic**: Data Validation 

🛠️ **SDK & DTO**: Service Communication

💻 **CLI**: CRUD Operations

🧩**Dependency Injection**: DB Session Management 

📊 **Decorator & Logger**: Monitor

📦 **PyPI & egg file** 

🧪 **Pytest, Mocking**: Testing

🔐 **Pagination**: API Design


🛡️ **Battle-tested**: Trusted by top companies like FAANG, Tenable, Wiz, and Palo Alto Networks.

Ready for production with a strong DevOps foundation.
