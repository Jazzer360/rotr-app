FROM python:3.12-slim

WORKDIR ~/app
COPY . .

RUN ls -a

RUN pip install --no-cache-dir -r requirements.txt

# Optionally set up for redis backend
# ENV REDIS_URL="redis://10.41.139.3:6379"

# Needed until Reflex properly passes SIGTERM on backend.
STOPSIGNAL SIGKILL

CMD reflex run --env prod --backend-only --backend-port ${PORT:-8000}
