# devops-with-kubernetes


kubectl config set-context --current --namespace=dwk-todos

k3d cluster create --api-port 6550 --port '8082:30080@agent[0]' -p 8081:80@loadbalancer --agents 2


## Links
- https://www.digitalocean.com/community/meetup_kits/getting-started-with-containers-and-kubernetes-a-digitalocean-workshop-kit
- https://hackersandslackers.com/flask-application-factory/
- https://hackersandslackers.com/your-first-flask-application