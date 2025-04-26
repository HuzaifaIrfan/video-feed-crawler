# video-feed-crawler


## Celery Worker

```sh
celery -A celery_app worker --loglevel=info
```

## Celery Beat

```sh
celery -A celery_app beat --loglevel=info
```