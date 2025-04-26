

from celery import Celery

app = Celery('video_feed_crawler')
app.config_from_object('celeryconfig')

# Manually import tasks
import tasks.crawler_tasks

app.conf.beat_schedule = {
    'crawl-pages-every-1-minute': {
        'task': 'tasks.crawler_tasks.crawl_pages',
        'schedule': 60.0,  # every 60 seconds
    },
}
app.conf.timezone = 'UTC'

# # Auto-discover tasks from the 'tasks' package
# app.autodiscover_tasks(['tasks'])