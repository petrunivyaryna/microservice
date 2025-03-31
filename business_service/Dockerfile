FROM python:3.11

WORKDIR /business_service

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8001

CMD ["uvicorn", "business_service:app", "--host", "0.0.0.0", "--port", "8001"]
