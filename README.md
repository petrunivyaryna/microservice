# Sentiment Analysis Microservice

This project consists of three interconnected microservices:
- **Client Service** (Handles user requests and authentication)
- **Database Service** (Stores and retrieves tweet sentiment data)
- **Business Logic Service** (Performs sentiment analysis)

All services communicate using HTTP requests and are containerized with Docker.

---

## Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/petrunivyaryna/microservice.git
cd microservice
```

### 2. Install Docker & Docker Compose
Windows/Mac: Install Docker Desktop (https://www.docker.com/products/docker-desktop/).

### 3. Build & Run the Services
```bash
docker-compose up --build -d
```

Check if all services are running:
```bash
docker ps
```
You should see containers for `client_service`, `database_service` and `business_service`.
