FROM python:3.12-slim

WORKDIR ~/app
COPY . .

RUN pip install --no-cache-dir -r requirements.txt

# Optionally set up for redis backend
# ENV REDIS_URL="redis://10.41.139.3:6379"
ENV API_URL="https://localhost:8000"
ENV PYTHONBUFFERED=1
ENV REFLEX_ENV=production

ENTRYPOINT reflex run --env prod --backend-only --backend-port ${PORT:-8000}
