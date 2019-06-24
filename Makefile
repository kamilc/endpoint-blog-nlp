SHELL := /bin/bash
VERSION?=latest
TASK_IMAGES:=$(shell find tasks -name Dockerfile -printf '%h ')
REGISTRY=base:5000

tasks/%: FORCE
	set -e ;\
	docker build -t blog_pipeline_$(@F):$(VERSION) $@ ;\
	docker tag blog_pipeline_$(@F):$(VERSION) $(REGISTRY)/blog_pipeline_$(@F):$(VERSION) ;\
  docker push $(REGISTRY)/blog_pipeline_$(@F):$(VERSION)

images: $(TASK_IMAGES)

start_notebooks:
	kubectl apply -f notebooks.yml

stop_notebooks:
	kubectl delete deployment jupyter-notebook

FORCE: ;
