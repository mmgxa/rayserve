FROM vllm/vllm-openai:v0.5.0

ARG HF_TOKEN

ENV HF_TOKEN=$HF_TOKEN

WORKDIR /app

ENV HF_HUB_ENABLE_HF_TRANSFER 1

RUN apt update && \
    apt install -y wget curl python3-pip

COPY requirements.txt .

# Upgrade pip
RUN pip install --no-cache-dir --upgrade pip \
    & pip install --no-cache-dir -r requirements.txt

RUN huggingface-cli download "google/gemma-2b-it" --revision float16

ENV HF_TOKEN=

# Expose ports
EXPOSE 8000

EXPOSE 8265

COPY main.py .
