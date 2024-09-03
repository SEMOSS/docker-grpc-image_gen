ARG BASE_REGISTRY=docker.io
ARG BASE_IMAGE=nvidia/cuda
ARG BASE_TAG=12.4.0-runtime-ubuntu22.04

FROM ${BASE_REGISTRY}/${BASE_IMAGE}:${BASE_TAG} as builder

LABEL maintainer="semoss@semoss.org"

RUN apt-get update && apt-get install -y \
    python3-pip \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

COPY ./model_files /model_files

ENV PYTHONPATH="/app/server"

EXPOSE 50051

CMD ["python3", "server/gRPC/grpc_server.py"]