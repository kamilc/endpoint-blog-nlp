SHELL := /bin/bash
VERSION?=latest

.PHONY: list
list:
	@$(MAKE) -pRrq -f $(lastword $(MAKEFILE_LIST)) : 2>/dev/null | awk -v RS= -F: '/^# File/,/^# Finished Make data base/ {if ($$1 !~ "^[#.]") {print $$1}}' | sort | egrep -v -e '^[^[:alnum:]]' -e '^$@$$'

.build/base_image_$(VERSION):
	set -e ;\
	docker build -t endpoint-blog-pipeline/base:$(VERSION) -t endpoint-blog-pipeline/base:latest tasks/base ;\
	touch .build/base_image_$(VERSION)

.build/notebooks_image_$(VERSION): .build/base_image_$(VERSION)
	set -e ;\
	docker build -t endpoint-blog-pipeline/notebooks:$(VERSION) -t endpoint-blog-pipeline/notebooks:latest tasks/notebooks ;\
	touch .build/notebooks_image_$(VERSION)

.build/orchestrator_image_$(VERSION):
	set -e ;\
	docker build -t endpoint-blog-pipeline/orchestrator:$(VERSION) -t endpoint-blog-pipeline/orchestrator:latest orchestrator ;\
	touch .build/orchestrator_image_$(VERSION)

images: .build/orchestrator_image_$(VERSION) .build/notebooks_image_$(VERSION)

docker_compose_yml:
	VERSION=$(VERSION) envsubst < "docker-compose.yml.template" > "docker-compose.yml" ;\

clean:
	rm -f .build/*

stop: docker_compose_yml
	set -e ;\
	docker-compose down ;\
	docker container prune --filter='label=luigi_task_id'

run: docker_compose_yml images
	CURRENT_UID=$$(id -u):$$(id -g) docker-compose up orchestrator

notebooks: docker_compose_yml images
	CURRENT_UID=$$(id -u):$$(id -g) docker-compose up notebooks
