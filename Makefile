NAME=api_out_of_the_box
DOCKER_NAME=laquay/$(NAME)
VERSION=1.0.0
DOCKER_NAME_FULL=$(DOCKER_NAME):$(VERSION)
DOCKER_LOCALHOST=$(shell ip addr show docker0 | grep -Po 'inet \K[\d.]+')
DOCKER_VOLUME=$(shell pwd)
DOCKER_VOLUME_REPORTS=$(shell pwd)/reports

clean:
	@find . -iname "*~" | xargs rm 2>/dev/null || true
	@find . -iname "*.pyc" | xargs rm 2>/dev/null || true
	@find . -iname "build" | xargs rm -rf 2>/dev/null || true

build: clean
	docker build -t $(DOCKER_NAME_FULL) ./backend

run: build
	docker run -it -p 5000:5000 \
	    --add-host postgres:$(DOCKER_LOCALHOST) \
	    --name $(NAME) \
	    --env-file backend/ENV/api.env --rm $(DOCKER_NAME_FULL)

run-tests: build
	docker run -i \
	    -v $(DOCKER_VOLUME_REPORTS):/opt/$(NAME)/reports \
	    --add-host mbpostgres:$(DOCKER_LOCALHOST) \
	    --name $(NAME) \
	    --env-file backend/ENV/test.env --rm $(DOCKER_NAME_FULL) "/opt/$(NAME)/scripts/run_tests"

publish: build
	docker push $(DOCKER_NAME_FULL)

setup:
	docker-compose -f docker-compose.yml up -d

setup-tests:
	docker-compose -f docker-compose.tests.yml -p tests up -d