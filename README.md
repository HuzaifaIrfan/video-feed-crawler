<br />

<div align="center">
  <h1>Video Feed Crawler</h1>
  <p><h3 align="center">Continuous Delivery of Selenium and Celery based Video Feed Crawler 🚀</h3></p>
</div>


•
<hr>
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

## 🤝🏻 &nbsp;Connect with Me

<p align="center">
<a href="https://www.huzaifairfan.com"><img src="https://img.shields.io/badge/-huzaifairfan.com-1aa260?style=flat&logo=Google-Chrome&logoColor=white"/></a>
<a href="https://www.linkedin.com/in/huzaifairfan/"><img src="https://img.shields.io/badge/-Huzaifa%20Irfan-0072b1?style=flat&logo=Linkedin&logoColor=white"/></a>
<a href="https://github.com/HuzaifaIrfan/"><img src="https://img.shields.io/badge/-Huzaifa%20Irfan-4078c0?style=flat&logo=Github&logoColor=white"/></a>
<a href="mailto:contact@huzaifairfan.com"><img src="https://img.shields.io/badge/-contact@huzaifairfan.com-c71610?style=flat&logo=Gmail&logoColor=white"/></a>
</p>

## License

Licensed under the MIT License, Copyright 2025 Huzaifa Irfan. [LICENSE](LICENSE)