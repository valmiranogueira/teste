kubectl delete pod api
kubectl delete service api
docker build -t api .
kubectl create -f api.yaml
kubectl create -f api-expose.yaml