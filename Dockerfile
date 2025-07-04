FROM python:3.13-slim

WORKDIR /app
COPY . .

RUN pip install --no-cache-dir -r requirements.txt

# Optionally set up for redis backend
# ENV REDIS_URL="redis://10.41.139.3:6379"
ENV PYTHONUNBUFFERED=1
ENV REFLEX_ENV=production

CMD ["reflex", "run", "--env", "prod", "--backend-only", "--backend-port", "8080"]
