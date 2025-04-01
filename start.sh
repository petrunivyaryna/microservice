#!/bin/bash

echo "Building and starting services..."
docker-compose up --build -d

echo "All services are running!"
docker ps
