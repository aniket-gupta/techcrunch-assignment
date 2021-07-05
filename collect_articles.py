from config import Config
from server.db import create_tables
from server.celery.tasks import fetch_post

if __name__ == '__main__':
    if Config.CREATE_TABLES:
        create_tables()
    for i in range(1, Config.NUM_ARTICLES//10 + 1):
        # create async task
        fetch_post.delay(i)
