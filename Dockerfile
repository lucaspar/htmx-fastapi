FROM docker.io/pfeiffermax/python-poetry:1.8.0-poetry1.7.1-python3.11.6-slim-bookworm
WORKDIR /app

# copy only project dependencies for caching
COPY poetry.lock pyproject.toml /app/
RUN poetry install --no-root

# add the other project files
ADD . /app

# make port 8000 available to the world outside this container
EXPOSE 8000

# run main.py when the container launches
CMD ["python", "app/main.py"]
