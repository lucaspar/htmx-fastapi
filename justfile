# Variables
env_file := "docker/docker.env"
compose_file := "docker/compose.yaml"

alias dev := develop

# redeploys the application
redeploy: pull build down up-daemon logs

# starts the development server
develop: pull build down up-dev

# stops the application
down:
    docker compose --env-file={{env_file}} --file={{compose_file}} down

# pulls the latest images
pull:
    docker compose --env-file={{env_file}} --file={{compose_file}} pull --ignore-buildable

# builds the application
build:
    docker compose --env-file={{env_file}} --file={{compose_file}} build

# starts the application in daemon mode
up-daemon:
    docker compose --env-file={{env_file}} --file={{compose_file}} up -d

# starts the application in development mode
up-dev:
    docker compose --env-file={{env_file}} --file={{compose_file}} up --watch

# shows the logs
logs:
    docker compose --env-file={{env_file}} --file={{compose_file}} logs -f

# runs the tests
test:
    uv run --dev pytest --strict-config --capture=no
