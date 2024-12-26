## 1. Install Docker
Visit the [Docker Docs](https://docs.docker.com/desktop/setup/install/linux/) to install Docker for your OS.

## 2. Install nvidia-toolkit
Visit the [NVIDIA](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html#installing-with-apt) Container Toolkit documentation to get NVIDIA runtime setup for Docker.


# Satu-1
```
 docker run --rm --runtime=nvidia --gpus all -e CACHE_DIRECTORY=/root/models  -v ~/.kuzco/models:/root/models kuzcoxyz/amd64-ollama-nvidia-worker --worker vBeNhW2MTYZwWbJRx94Ho --code 568dd654-cf57-4a92-a768-1ba4b892b9e7
```
