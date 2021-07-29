# Kubernetes, Docker annd Python API test

## Starting the API

### Requirements

**Docker**
**Python 3+**
**Kubernetes cluster** - See more about instalation of Minikube, k3s, Microk8s or Kind
**Linux OS or WSL**

### Command to run

``` cd api && sh run_api.sh ````

This command will create a Dockerfile and start an API pod in the Kubernetes cluster, under current namespace.

**It's required that the cluster works with Docker local images**
