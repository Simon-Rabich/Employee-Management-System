# 🚀 Employee Management System
# Fully Customized RESTFul API App

## Update Docker Image (build, tag and push)
```bash
docker build -t simon658/fastapi-app:latest .
docker push simon658/fastapi-app:latest
docker images
docker login
```

## Alembic DB Migration
```bash
alembic revision --autogenerate -m "Add product_version table"
alembic upgrade head
```
## 1. CLI App (CRUD actions)
```bash
python main.py
```
## 2. DB
```bash
psql -U simonravitz -h localhost postgres
```
## 3. FastAPI
```bash
uvicorn src.main:app --host 0.0.0.0 --port 8000
```
## Log time Decorator in endpoint
```bash
Run on: 2024-09-11 18:57:10
------------------------------
INFO:     127.0.0.1:61362 - "GET /api/employees HTTP/1.1" 200 OK
```
## Pydantic and DTO
```bash
from pydantic import BaseModel

class HealthCheckDTO(BaseModel):
    status: str
    version: str = None
    buildTime: str = None
```
## SDK
```bash


```
## 4. docker-compose
```bash
docker-compose up --build
```
## 5. Kubernetes
```bash
minikube start
```
## 6. Run application in k8s
```bash
kubectl port-forward svc/fastapi-app-new-employee-app 8081:80
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
docker exec -it nexus cat /nexus-data/admin.password
```
## Deploy or Upgrade with Helm Chart
```bash
helm upgrade --install employee-management-system ./helm
 kubectl apply -f deployment.yaml
 docker pull simon0101/employee-management-system-web:latest

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
 helm install employee-management-system ./helm --debug --dry-run
```
## 📦 Installation
```bash
pip install employee_management_system
```
## API Docs
```bash
Swagger
```
## EKS Cluster - Prometheus & Grafana, Monitoring Service
```bash
kubectl --namespace=prometheus port-forward deploy/prometheus-server 9090:9090
kubectl --namespace grafana port-forward $POD_NAME 3000:3000
```
## Pagination
```bash
xxxxx
```
## CI workflow
```bash
GitHub Actions
```
## KubeApps
```bash
kubectl port-forward -n kubeapps svc/kubeapps 8080:80
kubectl port-forward svc/worthless-belief-wordpress 8083:80 --namespace default
```
## Image, services, deployments and pods
```bash
```
## Service Design
```bash

```
## Tests
```bash
```