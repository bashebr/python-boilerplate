FROM python:3.12-slim AS builder

RUN pip install uv
WORKDIR /app

COPY . .
RUN uv sync --frozen --no-dev


FROM python:3.12-slim
WORKDIR /app

COPY --from=builder /app /app
ENV PYTHONUNBUFFERED=1
ENV PATH="/app/.venv/bin:$PATH"

CMD ["uvicorn", "python_boilerplate.web:app", "--host", "0.0.0.0", "--port", "8000"]
