import logging

from server.db.models import Author, Article
from server.exceptions import NotFound, BadRequest


class Repository:

    def __init__(self, session):
        self._session = session


class ArticleRepository(Repository):

    def get_article_by_id(self, article_id):
        article = self._session.query(Article).\
            filter(Article.id == int(article_id)).\
            first()
        if not article:
            raise NotFound(f'article {article_id} not found')
        return article.as_dict()

    def get_articles_by_author_name(self, author_name, offset=0, limit=10):
        logging.info(f'offset={offset}')
        logging.info(f'limit={limit}')
        logging.info(f'author_name={author_name}')
        if offset < 0 or limit <= 0:
            raise BadRequest("incorrect query parameters")
        if limit > 100:
            limit = 100
        q = self._session.query(Article). \
            join(Author, Article.author_id == Author.id). \
            filter(Author.name == author_name)
        count = q.count()
        if count == 0:
            raise NotFound(f'articles with author name {author_name} not found')
        if offset >= count or offset < 0 or limit <= 0:
            raise BadRequest("incorrect query parameters")
        articles = q.offset(offset).limit(limit).all()
        if not articles:
            return []
        article_list = [article.as_dict() for article in articles]
        return {
            "total_articles": count,
            "offset": offset,
            "limit": len(article_list),
            "articles": article_list,
        }

    def get_articles(self, offset=0, limit=10):
        count = self._session.query(Article).count()
        if count == 0:
            return {
                "total_articles": 0,
                "articles": [],
            }
        if offset >= count or offset < 0 or limit <= 0:
            raise BadRequest("incorrect query parameters")
        if limit > 100:
            limit = 100
        articles = self._session.query(Article).\
            offset(offset).\
            limit(limit).all()
        if not articles:
            return {
                "total_articles": 0,
                "articles": [],
            }
        article_list = [article.as_dict() for article in articles]
        return {
            "total_articles": count,
            "offset": offset,
            "limit": len(article_list),
            "articles": article_list,
        }


class AuthorRepository(Repository):

    def get_author_by_id(self, author_id):
        author = self._session.query(Author).\
            filter(Author.id == int(author_id)).first()

        if not author:
            raise NotFound(f'author {author_id} not found')
        return author.as_dict()

    def get_author_by_name(self, author_name):
        author = self._session.query(Author).\
            filter(Author.name == int(author_name)).first()
        if not author:
            raise NotFound(f'author {author_name} not found')
        return author.as_dict()

    def get_authors(self, offset=0, limit=10):
        count = self._session.query(Author).count()
        if count == 0:
            return {
                "total_authors": 0,
                "authors": [],
            }
        if offset >= count or offset < 0 or limit <= 0:
            raise BadRequest("incorrect query parameters")
        if limit > 100:
            limit = 100
        authors = self._session.query(Author).\
            offset(offset).limit(limit).all()
        if not authors:
            return {
                "total_authors": 0,
                "authors": [],
            }
        author_list = [author.as_dict() for author in authors]
        return {
            "total_authors": count,
            "offset": offset,
            "limit": len(author_list),
            "authors": author_list,
        }


