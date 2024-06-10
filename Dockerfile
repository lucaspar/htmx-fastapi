# https://hub.docker.com/r/thehale/python-poetry/tags
FROM docker.io/thehale/python-poetry:1.8.3-py3.12-slim
WORKDIR /app

# copy only project dependencies for caching
COPY poetry.lock pyproject.toml /app/
RUN poetry check

# add the other project files
ADD . /app

# make port 8000 available outside this container
EXPOSE 8000
