# FastAPI + HTMX

This is a simple FastAPI application that serves an HTMX front-end.

## Setup

```bash
docker compose up --build
```

The application will be available at [`localhost:18000`](http://localhost:18000).

## Development

```bash
poetry install --sync
```

### Development Server

```bash
poetry run uvicorn src.main:app --reload --port 8001
```

Access the application at [`localhost:8001`](http://localhost:8001).

### Testing

```bash
poetry run pytest --strict-config --capture=no
```

## Usage

Navigate to `http://localhost:8000` in your web browser to view the HTMX front-end.

## License

[MIT](https://choosealicense.com/licenses/mit/)
