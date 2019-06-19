SHELL := /bin/bash
VERSION?=latest
task_images:=$(shell find tasks -name Dockerfile -printf '%h ')

tasks/%: FORCE
	docker build -t blog_pipeline_$(@D):$(VERSION) $@

images: $(task_images)
	echo $(task_images)

FORCE: ;
