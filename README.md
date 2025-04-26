# video-feed-crawler

## Setup

- Ubuntu 24.04
- Docker
- VS Code

## Code

- Use VS Code Dev Container
- Environment Setup is given in [.devcontainer/docker-compose.yml](.devcontainer/docker-compose.yml)

## Install Libs

```sh
uv sync
```

## TEST

```sh
uv run pytest
```

## RUN

### Celery Worker

```sh
celery -A celery_app worker --loglevel=info
```

### Celery Beat

```sh
celery -A celery_app beat --loglevel=info
```


## Docker Build Test

- Run Outside Dev Container

### Build
```sh
docker compose build
```

### Test
```sh
docker compose run --rm video_feed_crawler uv run pytest
```

### Down
```sh
docker compose down
```
