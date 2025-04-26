
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from dotenv import load_dotenv
import os

# Load the .env file
load_dotenv(override=True)

# Access environment variables
CELERY_BROKER_URL = os.getenv("CELERY_BROKER_URL", "redis://localhost:6379/0")
print(f"CELERY_BROKER_URL at '{CELERY_BROKER_URL}'")

from celery import Celery

app = Celery('video_feed_crawler', broker=CELERY_BROKER_URL,backend=CELERY_BROKER_URL)


# Manually import tasks
import tasks.math_tasks

app.conf.beat_schedule = {
    'run-every-1-minute': {
        'task': 'tasks.math_tasks.print_time',
        'schedule': 6.0,  # every 60 seconds
    },
}
app.conf.timezone = 'UTC'

# # Auto-discover tasks from the 'tasks' package
# app.autodiscover_tasks(['tasks'])