import pytest
from celery import Celery
from multiprocessing import Process
import time

from celery_app import app as celery_app_

@pytest.fixture(scope='session')
def celery_app():
    return celery_app_

@pytest.fixture(scope='session', autouse=True)
def celery_worker(celery_app):
    def start_worker():
        celery_app.worker_main([
            'worker',
            '--loglevel=info',
            '--pool=solo'  # Important: 'solo' for subprocess-friendly
        ])

    worker = Process(target=start_worker)
    worker.start()
    time.sleep(2)  # wait for the worker to start

    yield

    worker.terminate()
    worker.join()
