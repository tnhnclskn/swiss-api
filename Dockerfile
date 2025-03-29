FROM python:3.13-slim

RUN apt-get update && apt-get install -y build-essential && apt-get clean

RUN pip install --upgrade pip

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 3000

CMD ["python", "app.py"]