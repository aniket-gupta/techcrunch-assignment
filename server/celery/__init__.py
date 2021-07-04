from celery import Celery

celery_app = Celery('techcrunch',
                    broker='redis://localhost:6379',
                    backend='redis://localhost:6379',
                    include=['server.celery.tasks'])