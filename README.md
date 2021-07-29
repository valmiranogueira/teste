# Kubernetes, Docker and Python API test

## Starting the Companies API

### Requirements

- Docker
- Python 3+
- Kubernetes cluster:  See more about instalation of Minikube, k3s, Microk8s or Kind
- Linux OS or WSL

### Command to run

`cd api && sh run_api.sh`

This command will create a Dockerfile and start an API pod in the Kubernetes cluster, under current namespace.

**It's required that the cluster works with Docker local images**

### Exercise 1

Create an Python API that responds to /test_api(Flask recommended, but feel free with other Python modules).

This API must receive data as JSON with keys: url and status code. The output must be the result of an GET HTTP request to the provided url and check if the status code of the request is the same as provided in payload.

To test it with Companies API, find the pod called "api" (you will find the pod IP) and then:

`curl http://api_ip:5000/companies`

The output of Companies API is something like this:

`[{"id": 1, "name": "Company One"}, {"id": 2, "name": "Company Two"}]`

The status code of the request is 200

### Exercise 2

Create a Docker image adding the API created in exercise 1. The build will save the image under the localhost.

### Exercise 3

Create a pod that will run image created in exercise 2.

### Exercise 4

Test the API running on pod created in exercise 3. This test must be performed 
