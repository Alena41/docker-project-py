FROM python:3.14-slim AS builder

WORKDIR /build
COPY requirements.txt .
RUN pip install --no-cache-dir --prefix=/install -r requirements.txt

FROM python:3.14-slim

# non-root пользователь
RUN useradd -r -u 1001 appuser

WORKDIR /app
COPY --from=builder /install /usr/local
COPY app.py .

USER appuser
EXPOSE 8080

ENTRYPOINT ["python", "app.py"]