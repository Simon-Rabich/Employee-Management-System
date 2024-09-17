# 🚀 Employee Management System
# Fully Customized RESTFul API App

## Rebuild and Push Docker Image
```bash
docker build -t simon658/fastapi-app:latest .
docker push simon658/fastapi-app:latest
```
## Update the Deployment in Kubernetes
```bash
values.yaml

image:
  repository: simon658/fastapi-app
  tag: latest
  pullPolicy: Always
```
## Update Helm Chart
```bash
helm upgrade --install fastapi-app ./helm --namespace default
kubectl rollout restart deployment fastapi-app-new-employee-app -n default
```
## DB Migration
```bash
alembic revision --autogenerate -m "Add product_version table"
alembic upgrade head
```
## CLI App with CRUD Actions
```bash
python main.py
```
## DB Connection
```bash
psql -U simonravitz -h localhost postgres
```
## DB Session
```bash
handling the database session using the Depends(get_db) pattern, which is typical for managing database sessions in FastAPI. The Depends(get_db) injects a database session (Session) into the route function and ensures that the session is available for the duration of the request.
```
## FastAPI
```bash
uvicorn src.main:app --host 0.0.0.0 --port 8000 || uvicorn src.main:app --reload
```
## Decorator
```bash
@log_datetime

e.g:
Run on: 2024-09-11 18:57:10
------------------------------
INFO:     127.0.0.1:61362 - "GET /api/employees HTTP/1.1" 200 OK
```
## Pydantic & DTO
```bash
from pydantic import BaseModel

class HealthCheckDTO(BaseModel):
    status: str
    version: str = None
    buildTime: str = None
```
## SDK
```bash
e.g:
health_response = client.get_health(environment=environment)
```
## 4. docker-compose
```bash
docker-compose up --build
```
## 5. Kubernetes
```bash
minikube start
```
## 6. Run App in k8s
```bash
kubectl port-forward svc/fastapi-app-new-employee-app 8081:80 -n default
```
## GitOps using ArgoCD
```bash
kubectl port-forward svc/argocd-server -n argocd 8083:443
```
## Get Password for ArgoCD UI 
```bash
 argocd admin initial-password -n argocd
```
## Paging & API Schema Response
```bash

```
## Nexus - Artifact Register Repository
```bash
/usr/local/nexus/bin/nexus start
docker exec -it nexus cat /nexus-data/admin.password
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