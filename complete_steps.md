# Setup


## 1. Create Kubernetes Cluster

Install tools like minikube (local only) or eksctl (eks only), helm, kubectl, k9s.

Is using minikube, don't forget to enable GPU support via
```bash
sudo nvidia-ctk runtime configure --runtime=docker && sudo systemctl restart docker
```

Then start minikube via
```bash
minikube start --driver=docker --container-runtime docker --gpus all ...
```
## 2. Install the KubeRay operator

```bash
helm repo add kuberay https://ray-project.github.io/kuberay-helm/
helm repo update

helm install kuberay-operator kuberay/kuberay-operator --version 1.1.1

kubectl get pods
```

## Create RayService

```bash
kubectl apply -f ray-service.yaml
```

## Status

```
kubectl get rayservice # Service should be running
kubectl get raycluster # check desired andrunning workers
kubectl get pods -l=ray.io/is-ray-node=yes
kubectl get services
# to see dashboard
kubectl port-forward svc/rayservice-sample-head-svc --address 0.0.0.0 8080:8265
# for inference
kubectl port-forward service/rayservice-llm-serve-svc  --address 0.0.0.0 8000:8000
```

## Test Inference

```bash
python test.py
```

## Benchmark Inference

```bash
# inside the benchmark folder
wget https://huggingface.co/datasets/anon8231489123/ShareGPT_Vicuna_unfiltered/resolve/main/ShareGPT_V3_unfiltered_cleaned_split.json

python benchmark_serving.py \
        --backend openai-chat \
        --model "google/gemma-2b-it" \
        --tokenizer "google/gemma-2b-it" \
        --dataset-name sharegpt \
        --dataset-path ./ShareGPT_V3_unfiltered_cleaned_split.json \
        --request-rate 5 \
        --num-prompts 5 \
        --save-result \
        --endpoint "/v1/chat/completions"
```