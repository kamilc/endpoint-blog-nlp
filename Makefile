SHELL := /bin/bash
VERSION?=latest
TASK_IMAGES:=$(shell find tasks -name Dockerfile -printf '%h ')

tasks/%: FORCE
	docker build -t blog_pipeline_$(@D):$(VERSION) $@

images: $(TASK_IMAGES)

FORCE: ;
