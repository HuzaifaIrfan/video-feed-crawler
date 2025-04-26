import pytest
from database import Database
from tasks.crawler_tasks import crawl_pages


# @pytest.mark.usefixtures("celery_worker")
def test_crawl_pages_task(celery_app):
    Database().clean_videos()
    result = crawl_pages.delay()
    inserted_videos=result.get(timeout=30)
    print(f"inserted_videos {inserted_videos}")
    assert len(inserted_videos) > 0
