DIRNAME := $(shell basename $$(pwd))
HOME := $(shell echo $$HOME)

help:
	echo "Synopsis: make [init up down web db clean bkup reset]"

test:
	echo $(DIRNAME)
	echo $(HOME)

build:
	docker build -t $(DIRNAME) src

run:
	docker run -it --rm --mount type=bind,src=$(HOME),dst=/home $(DIRNAME)

dev: build run

clean:
	docker container prune -f
	docker images | awk '/software_modules/ {print $$3}' | xargs -r docker rmi
	docker system prune -f
