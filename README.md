# 🚀 Employee Management System

A FastAPI-based Employee Management System with DevOps integrations.

## 📦 Usage

```bash
1. python main.py
2. psql -U simonravitz -h localhost postgres
3. uvicorn src.main:app --host 0.0.0.0 --port 8000
4. docker-compose up --build
5. **minikube start**
6. kubectl port-forward deployment/employee-management-system 8080:8000
Argo CD - GitOps:
7. kubectl port-forward svc/argocd-server -n argocd 8081:443
8. /usr/local/nexus/bin/nexus start
Deploy or Upgrade with Helm:
9. helm upgrade --install employee-management-system ./helm-employee-management-system
 helm status employee-management-system

Logs: 
helm install employee-management-system ./helm-employee-management-system --debug --dry-run

Verify the Deployment:

kubectl get pvc
kubectl get pods
kubectl get svc



```
## 📦 Installation

```bash
pip install employee_management_system
```

## 🛠️ Tools
DATA BASE, ASGI, K8S, HELM Chart, DOCKER COMPOSE, REST API FRAMEWORK, API RESPONSE and DTO, SDK, CLI 
Services layers: Services > Controllers > Data Access Layer  

Argo CD

🔄 **Alembic** DB Migration 

🔗 **SQLAlchemy**

🐘 **Postgres**

⚡  **FastAPI** 

📄 **Swagger OpenAPI** 

🔧 **GitHub Actions** 

🐳 **Docker Compose

**Dockerfile**: Rapid Setup & Containerization 

🚀 **Uvicorn**: ASGI Web Server

🔐 **Pydantic**: Data Validation 

🛠️ **SDK**: Service Communication 

💻 **CLI Tool**: CRUD Operations 

🧩**Dependency Injection**: DB Session Management 

📊 **Decorator & Logger** Monitor End Points

📦 **PyPI** egg file 

🧪 **Pytest, Mocking** Testing

🔐 **Pagination**
=======
## 🛠️ Features & Tools

- 🔄 **Alembic**: DB Migration
- 🔗 **SQLAlchemy**: ORM
- 🐘 **Postgres**: DB
- ⚡ **FastAPI**: REST Framework
- 📄 **Swagger OpenAPI**: Interactive API Docs
- 🔧 **GitHub Actions**: CI
- 🐳 **Docker Compose & Dockerfile**: Rapid Setup & Containerization
- 🚀 **Uvicorn**: ASGI Web Server
- 🔐 **Pydantic**: Data Validation
- 🛠️ **SDK**: Service Communication
- 💻 **CLI Tool**: CRUD Operations
- 🧩 **Dependency Injection**: DB Session Management
- 📊 **Logger & Decorators**: Monitoring & Observability
- 📦 **PyPI**: WIP
- 🧪 **Testing**: Pytest, Mocking
- 🔐 **Pagination**: WIP

### 📑 **Pagination**
*WIP*



🛡️ **Battle-tested**: Trusted by top companies like FAANG, Tenable, Wiz, and Palo Alto Networks.

Ready for production with a strong DevOps foundation.

