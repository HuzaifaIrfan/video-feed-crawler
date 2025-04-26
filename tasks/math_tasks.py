# tasks/math_tasks.py
from celery_app import app

@app.task(name='tasks.math_tasks.print_time')  # <<< Important!
def print_time():
    from datetime import datetime
    print(f"Current time is: {datetime.now()}")
