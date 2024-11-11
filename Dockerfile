FROM python:3.12-slim
WORKDIR ~/app
COPY . .
RUN ls -a

ENV PATH="~/app/.venv/bin:$PATH" PYTHONUNBUFFERED=1

# Optionally set up for redis backend
# ENV REDIS_URL="redis://10.41.139.3:6379"

# Needed until Reflex properly passes SIGTERM on backend.
STOPSIGNAL SIGKILL

CMD reflex run --env prod --backend-only --backend-port ${PORT:-8000}
