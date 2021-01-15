# dev

.PHONY: black
black: ## black formatter
	black dwk-todos/
	black dwk-frontend/

# k8s

.PHONY: namespace-apply
namespace-apply: ## Apply dwk deployment
	kubectl apply -f k8s/namespace-dwk-todos.yaml

.PHONY: namespace-delete
namespace-delete: ## Apply dwk deployment
	kubectl delete -f k8s/namespace-dwk-todos.yaml

.PHONY: db-apply
db-apply: ## Apply dwk deployment
	kubectl apply -f db/postgres-ss.yml
	kubectl apply -f db/postgres-svc.yml

.PHONY: db-delete
db-delete: ## Apply dwk deployment
	kubectl delete service postgres-svc
	kubectl delete statefulsets.apps postgres-ss

.PHONY: todos-apply
todos-apply: ## Apply dwk deployment
	# dwk-frontend
	kubectl apply -f dwk-frontend/k8s/deployment.yaml
	kubectl apply -f dwk-frontend/k8s/service.yaml
	kubectl apply -f dwk-frontend/k8s/ingress.yaml
	# dwk-todos
	kubectl apply -f dwk-todos/k8s/deployment.yaml
	kubectl apply -f dwk-todos/k8s/service.yaml

.PHONY: todos-delete
todos-delete: ## Apply dwk deployment
	# dwk-frontend
	kubectl delete ingress dwk-frontend-ingress
	kubectl delete service dwk-frontend-svc
	kubectl delete deployment dwk-frontend-deploy
	# dwk-todos
	kubectl delete service dwk-todos-svc
	kubectl delete deployment dwk-todos-deploy

.PHONY: apply-all
apply-all: db-apply todos-apply ## Apply dwk deployment

.PHONY: delete-all
delete-all: todos-delete db-delete ## Apply dwk deployment
