# FastAPI + HTMX

This is a simple FastAPI application that serves an HTMX front-end.

## Setup

```bash
docker compose up --build
```

The application will be available at [`localhost:18000`](http://localhost:18000).

## Development

```bash
# install packages locally for local editor linter, formatter, etc
uv sync --dev

# start the development server
make develop
```

Access the application at [`localhost:18000`](http://localhost:18000).

> Port 18000 is configurable in [`docker.env`](docker.env).

### Testing

```bash
# install uv in the host machine to run the tests
make test
```

## Usage

Navigate to `http://localhost:8000` in your web browser to view the HTMX front-end.
