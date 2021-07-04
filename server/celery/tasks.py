from datetime import datetime

from server.celery import celery_app
from celery.exceptions import Reject
import requests

from server.db import Session
from server.db.models import Article, Author

POST_API = 'https://techcrunch.com/wp-json/wp/v2/posts?page={page_num}'
AUTHOR_API = 'https://techcrunch.com/wp-json/tc/v1/users/{author_id}'


@celery_app.task
def fetch_post(page_num):
    """
    fetch posts from techcrunch server using wordpress api
    :param page_num: page num to fetch
    :return:
    """
    req = POST_API.format(page_num=page_num)
    try:
        response = requests.get(req)
        response.raise_for_status()
        posts = response.json()
        objects = list()
        for json_post in posts:
            fetch_author.delay(json_post.get('author'), json_post.get("_links", dict()).get('authors', []))
            post = Article(id=json_post.get('id'),
                           date=json_post.get('date_gmt', datetime.now()),
                           modified=json_post.get('modified_gmt', datetime.now()),
                           title=json_post.get('title', dict()).get('rendered', ""),
                           content=json_post.get('content', dict()).get('rendered', ""),
                           author_id=json_post.get('author')
                           )
            objects.append(post)
        s = Session()
        s.bulk_save_objects(objects)
        s.commit()

    except requests.exceptions.HTTPError as error:
        raise Reject(error)
    except Exception as ex:
        raise Reject(ex)


@celery_app.task
def fetch_author(author_id, alternatives):
    """
    fetch author detail from techcrunch server using wordpress api
    :param author_id: author id to fetch
    :param alternatives: alternative uri in case of error
    :return:
    """
    if author_id:
        req = AUTHOR_API.format(author_id=author_id)
        try:
            response = requests.get(req)
            response.raise_for_status()
            author_data = response.json()
            save_author(author_data)

        except requests.exceptions.HTTPError as error:
            if len(alternatives) and alternatives[0].get('href'):
                try:
                    response = requests.get(alternatives[0].get('href'))
                    author_data = response.json()
                    author_data['id'] = author_id
                    save_author(author_data)
                except Exception as e:
                    raise Reject(error)


def save_author(author_data):

    author = Author(id=author_data.get("id"),
                    name=author_data.get("name"),
                    description=author_data.get("cbDescription"),
                    avatar=author_data.get("cbAvatar"),
                    position=author_data.get('position'),
                    links=author_data.get('links'),
                    twitter=author_data.get('twitter'))
    s = Session()
    if not s.query(Author.id).filter(Author.id == author_data.get("id")).first():
        s.add(author)
        s.commit()