FROM python:3.11

WORKDIR /client_service

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "-m", "uvicorn", "client_service:app", "--host", "0.0.0.0", "--port", "8003"]
