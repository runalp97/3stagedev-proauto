FROM python:3.9-slim
# Install curl and any other dependencies
RUN apt update && apt install -y curl
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "app.py"]
