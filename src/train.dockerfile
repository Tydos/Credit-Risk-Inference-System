# Training server
# Runs: python -m src.main
# Expects volumes from docker-compose.yml:
#   ./dataset:/app/dataset:ro
#   ./config:/app/config:ro

FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir torch --index-url https://download.pytorch.org/whl/cpu
    
RUN pip install --no-cache-dir \
    pandas \
    scikit-learn \
    pyyaml \
    pydantic \
    matplotlib \
    tqdm \
    mlflow \
    boto3

COPY src/ src/

CMD ["python", "-m", "src.main"]