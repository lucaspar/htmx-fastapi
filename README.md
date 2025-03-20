# FastAPI + HTMX

This is a simple FastAPI application that serves an HTMX front-end.

The application will be available at [`localhost:18000`](http://localhost:18000).

## Development

```bash
# install packages locally for local editor linter, formatter, etc
uv sync --dev

# start the development server
make develop
```

Access the application at [`localhost:18000`](http://localhost:18000).

> Port 18000 is configurable in [`docker.env`](docker/docker.env).

### Testing

```bash
# install uv in the host machine to run the tests
make test
```
