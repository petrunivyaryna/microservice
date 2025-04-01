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

## Request Flow 
1. Client sends a request to **Client Service** with the id and text of a tweet.
2. **Client Service** checks if the sentiment is available in **Database Service** by the tweet id.
- If found, it returns the result.
- If not, it forwards the request to **Business Logic Service**.
3. **Business Logic Service** analyzes the tweet and returns a sentiment result.
4. **Client Service** saves the sentiment result in **Database Service**.
5. Client receives the response with the sentiment analysis.

### Example Flow
Client requests sentiment analysis for **tweet1**:
```bash
curl -X POST "http://0.0.0.0:8003/process-data?token=your_secret_token" \
     -H "Content-Type: application/json" \
     -d '{"key": "tweet1", "value": "This is an amazing product!"}'
```
**Client Service** checks if **tweet1** exists in **Database Service** →  If not found, **Client Service** forwards it to **Business Logic Service** → **Business Logic Service** analyzes and sends back the sentiment → **Client Service** saves the sentiment in **Database Service** and returns it to the user.

## API Endpoints
**Business Logic Service** (Port 8001; url `http://localhost:8001/`)
- `GET /` → Returns a short description of the service.
- `GET /health` → Check service status.
- `POST /process` → Perform sentiment analysis on a tweet.

**Database Service** (Port 8002; url `http://localhost:8002/`)
- `GET /` → Returns a short description of the service.
- `GET /health` → Check service status.
- `GET /get/{key}` → Retrieve stored sentiment.
- `POST /save-sentiment` → Save sentiment data.

**Client Service** (Port 8003; url `http://localhost:8003/`)
- `GET /` → Returns a short description of the service.
- `GET /health` → Check service status.
- `POST /process-data` → Process a tweet and return its sentiment.

## Authentication
The **Client Service** uses token-based authentication. Each request must include an authentication token.

Example request using curl:
```bash
curl -X POST "http://0.0.0.0:8003/process-data?token=your_secret_token" \
     -H "Content-Type: application/json" \
     -d '{"key": "tweet1", "value": "This is an amazing product!"}'
```

