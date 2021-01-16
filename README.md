# devops-with-kubernetes


kubectl config set-context --current --namespace=dwk-todos
kubectl config set-context --current --namespace=kube-system

k3d cluster create --api-port 6550 --port '8082:30080@agent[0]' -p 8081:80@loadbalancer --agents 2


kubectl apply -f https://github.com/bitnami-labs/sealed-secrets/releases/download/v0.13.1/controller.yaml --namespace=kube-system


## Links
- https://www.digitalocean.com/community/meetup_kits/getting-started-with-containers-and-kubernetes-a-digitalocean-workshop-kit
- https://hackersandslackers.com/flask-application-factory/
- https://hackersandslackers.com/your-first-flask-application
- https://github.com/bitnami-labs/sealed-secrets
- https://www.arthurkoziel.com/encrypting-k8s-secrets-with-sealed-secrets/
