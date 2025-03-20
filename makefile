.PHONY: down pull build up up-dev logs redeploy develop test

ENV_FILE=docker/docker.env
COMPOSE_FILE=docker/compose.yaml

redeploy: pull build down up-daemon logs
develop: pull build down up-dev

down:
	docker compose --env-file=$(ENV_FILE) --file=$(COMPOSE_FILE) down

pull:
	docker compose --env-file=$(ENV_FILE) --file=$(COMPOSE_FILE) pull --ignore-buildable

build:
	docker compose --env-file=$(ENV_FILE) --file=$(COMPOSE_FILE) build

up-daemon:
	docker compose --env-file=$(ENV_FILE) --file=$(COMPOSE_FILE) up -d

up-dev:
	docker compose --env-file=$(ENV_FILE) --file=$(COMPOSE_FILE) up --watch

logs:
	docker compose --env-file=$(ENV_FILE) --file=$(COMPOSE_FILE) logs -f

test:
	uv run --dev pytest --strict-config --capture=no
