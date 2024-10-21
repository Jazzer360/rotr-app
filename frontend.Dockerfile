FROM python:3.12

WORKDIR /app
COPY . .

RUN curl -LsSf https://astral.sh/uv/install.sh | sh
ARG uv=/root/.cargo/bin/uv
ENV VIRTUAL_ENV=/app/.venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
RUN $uv venv
RUN $uv pip install -r requirements.txt

ARG API_URL=https://rotr-app-763868835094.us-central1.run.app
ARG ROTR_COMPILE_ONLY=1
RUN reflex export --no-zip --frontend-only
