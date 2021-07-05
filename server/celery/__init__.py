from celery import Celery

from config import Config

celery_app = Celery('techcrunch',
                    broker=Config.CELERY_BROKER,
                    backend=Config.CELERY_BACKEND,
                    include=['server.celery.tasks'])