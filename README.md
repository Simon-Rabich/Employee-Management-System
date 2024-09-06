# 🚀 Employee Management System

A FastAPI-based Employee Management System with DevOps integrations.

## Update Docker Image (build, tag and push)
```bash
docker build -t simon0101/employee-management-system-web:latest .
docker push simon0101/employee-management-system-web:latest
docker images
docker login
```

## DB Migration
```bash
alembic revision --autogenerate -m "Add product_version table"
alembic revision --autogenerate -m "Add build_time column to ProductVersion table"
alembic upgrade head
```
## CLI App (CRUD actions)
```bash
python main.py
```
## PostgresSQL DB
```bash
psql -U simonravitz -h localhost postgres
```
## FastAPI - using Uvicorn, which is an ASGI (Asynchronous Server Gateway Interface) server
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
## Run K8S
```bash
kubectl port-forward deployment/employee-management-system 8080:8000
```
## ArgoCD (GitOps)
```bash
kubectl port-forward svc/argocd-server -n argocd 8081:443
```
## Get Password for ArgoCD UI 
```bash
 argocd admin initial-password -n argocd
```
## Nexus - Artifact Register Repository
```bash
/usr/local/nexus/bin/nexus start
```
## Deploy or Upgrade with Helm Chart
```bash
helm upgrade --install employee-management-system ./helm-employee-management-system
```
## Verify the Deployment
```bash
kubectl get deployments
kubectl get pods
kubectl describe deployment employee-management-system
```
## Check Helm Deploy
```bash
 helm status employee-management-system
```
## Logs
```bash
 helm install employee-management-system ./helm-employee-management-system --debug --dry-run
```
## 📦 Installation
```bash
pip install employee_management_system
```

## 🛠️ Tools

⚓ **Helm Chart**

🗄 **Nexus**

📦 **Kubernetes**

🚢 **ArgoCD**

🔄 **Alembic**

🔗 **SQLAlchemy**

🐘 **Postgres**

⚡  **FastAPI**

📄 **Swagger OpenAPI**

🔧 **GitHub Actions**

🐳 **Docker Compose**: Rapid Setup & Containerization

🐳 **Dockerfile**: Rapid Setup & Containerization

🚀 **Uvicorn**: ASGI Web Server

🔐 **Pydantic**: Data Validation 

🛠️ **SDK & DTO**: Service Communication

💻 **CLI**

🧩 **Dependency Injection**: DB Session Management 

📊 **Decorator & Logger**

📦 **PyPI & Egg file** 

🧪 **Pytest, Mocking**

🔐 **Pagination**

🛡️ **Battle-tested tools and tech**: Trusted by top companies like FAANG, Tenable, Wiz, and Palo Alto Networks.
