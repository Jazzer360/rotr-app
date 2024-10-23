FROM python:3.11 as init

# Install `uv` for faster package boostrapping
RUN curl -LsSf https://astral.sh/uv/install.sh | sh
ARG uv=/root/.cargo/bin/uv

# Copy local context to `/app` inside container (see .dockerignore)
WORKDIR /app
COPY . .
RUN mkdir -p /app/data /app/uploaded_files

# Create virtualenv which will be copied into final container
ENV VIRTUAL_ENV=/app/.venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
RUN $uv venv

# Install app requirements and reflex inside virtualenv
RUN $uv pip install -r requirements.txt

# Deploy templates and prepare app
RUN reflex init

# Stage 2: copy artifacts into slim image 
FROM python:3.11-slim
WORKDIR /app
RUN adduser --disabled-password --home /app reflex
COPY --chown=reflex --from=init /app /app

# Install libpq-dev for psycopg2 (skip if not using postgres).
RUN apt-get update -y && apt-get install -y libpq-dev && rm -rf /var/lib/apt/lists/*

USER reflex
ENV PATH="/app/.venv/bin:$PATH" PYTHONUNBUFFERED=1

# Optionally set up for redis backend
# ENV REDIS_URL="redis://10.41.139.3:6379"

# Needed until Reflex properly passes SIGTERM on backend.
STOPSIGNAL SIGKILL

RUN printenv

# Always apply migrations before starting the backend.
CMD [ -d alembic ] && reflex db migrate; \
    exec reflex run --env prod --backend-only --backend-port ${PORT:-8000}
