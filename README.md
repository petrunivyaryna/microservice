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

## API Endpoints
**Client Service**
Port 8003; url `http://localhost:8003/`
- `GET /health` → Check service status.
- `POST /process-data` → Process a tweet and return its sentiment (inout).

## Authentication
The **Client Service** uses token-based authentication. Each request must include an authentication token.

Example request using curl:
```bash
curl -X POST "http://0.0.0.0:8003/process-data?token=your_secret_token" \
     -H "Content-Type: application/json" \
     -d '{"key": "tweet1", "value": "This is an amazing product!"}'
```

