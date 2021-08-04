kubectl create namespace teste || true
kubectl config set-context --current --namespace=teste
kubectl delete pod api || true
kubectl delete service api || true
docker build -t api .
kubectl create -f api.yaml