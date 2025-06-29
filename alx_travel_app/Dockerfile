# Dockerfile
FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirement.txt .
RUN pip install --upgrade pip && pip install -r requirement.txt

COPY . .

CMD ["gunicorn", "alx_travel_app.wsgi:application", "--bind", "0.0.0.0:8000"]
