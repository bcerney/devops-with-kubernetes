

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
	black todo/

# .PHONY: run-dev
# run-dev: # Run flask locally
# 	flask run

# Docker

.PHONY: login
login: ## Login to Docker Hub
	docker login

.PHONY: build-latest
build-latest: ## Build docker image
	docker build -t bcerney/dwk-todos:latest .
	docker push bcerney/dwk-todos:latest

.PHONY: run-dev
run-dev: # Run flask locally
	docker run -p 5000:5000 bcerney/dwk-todos:latest
	

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
	# kubectl delete ingress flask-ingress
	kubectl delete service dwk-todos-svc
	kubectl delete deployment dwk-todos-deploy
	# kubectl delete persistentvolumeclaim flask-claim
	# kubectl delete persistentvolume flask-pv

.PHONY: rebuild
rebuild: delete build-latest apply ## Delete dwk deployment

