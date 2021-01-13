

.PHONY: compile
compile: ## Compile requirements
	pip install --upgrade pip
	pip-compile -U requirements.in


.PHONY: install
install: ## Install requirements
	pip install --upgrade pip
	pip install -r requirements.txt

.PHONY: black
black: ## black formatter
	black frontend/

# .PHONY: run-dev
# run-dev: # Run flask locally
# 	flask run

# Docker

.PHONY: login
login: ## Login to Docker Hub
	docker login

.PHONY: build-latest
build-latest: ## Build docker image
	docker build -t bcerney/dwk-frontend:latest .
	docker push bcerney/dwk-frontend:latest

.PHONY: run-dev
run-dev: # Run flask locally
	docker run -p 5000:5000 bcerney/dwk-frontend:latest
	

# k8s

.PHONY: apply
apply: ## Apply dwk deployment
	# kubectl apply -f k8s/persistentvolume.yaml
	# kubectl apply -f k8s/persistentvolumeclaim.yaml
	kubectl apply -f k8s/deployment.yaml
	kubectl apply -f k8s/service.yaml
	kubectl apply -f k8s/ingress.yaml

.PHONY: delete
delete: ## Delete dwk deployment
	kubectl delete ingress dwk-frontend-ingress
	kubectl delete service dwk-frontend-svc
	kubectl delete deployment dwk-frontend-deploy
	# kubectl delete persistentvolumeclaim flask-claim
	# kubectl delete persistentvolume flask-pv

.PHONY: rebuild
rebuild: delete build-latest apply ## Delete dwk deployment
