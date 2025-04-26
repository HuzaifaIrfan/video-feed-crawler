
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


broker_url = CELERY_BROKER_URL
result_backend = CELERY_BROKER_URL
task_serializer = 'json'
accept_content = ['json']
timezone = 'UTC'
enable_utc = True
