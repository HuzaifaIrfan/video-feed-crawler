
<div align="center">
  <h1>Video Feed Crawler</h1>
  <p><h3 align="center">Continuous Delivery of Selenium and Celery based Video Feed Crawler 🚀</h3></p>
</div>


•
<hr>

# 🛠️ Development

## Setup

- Ubuntu 24.04
- Docker
- VS Code

## Code

- Use VS Code Dev Container
- Environment Setup is given in [.devcontainer/docker-compose.yml](.devcontainer/docker-compose.yml)

# 🚀 Usage

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

# 📝 Documentation

# 📚 References


# 🤝🏻 Connect with Me

[![GitHub](https://img.shields.io/badge/Github-%23222.svg?style=for-the-badge&logo=github&logoColor=white)](https://github.com/HuzaifaIrfan/)
[![Website](https://img.shields.io/badge/Website-%23222.svg?style=for-the-badge&logo=google-chrome&logoColor==%234285F4)](https://www.huzaifairfan.com)

# 📜 License

Licensed under the GPL3 License, Copyright 2025 Huzaifa Irfan. [LICENSE](LICENSE)
