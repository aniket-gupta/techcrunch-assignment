from flask import Blueprint, request, jsonify

from server.db import Session
from server.repositories.techcrunch_repository import ArticleRepository

article_bp = Blueprint('article', __name__, url_prefix='/v1/articles')


@article_bp.route('/')
def get_articles():
    """
    get all articles.
    query params:
        author_name: if present filter article by given auther name
        offset: start offset for pagination. default 0
        limit: max number of articles to be return in results. default 10
    :return: list of articles
    """
    offset = int(request.args.get('offset', 0))
    limit = int(request.args.get('limit', 10))
    if 'author_name' in request.args:
        author_name = str(request.args['author_name'])
        return jsonify(ArticleRepository(Session()).get_articles_by_author_name(author_name, offset, limit))
    else:
        return jsonify(ArticleRepository(Session()).get_articles(offset, limit))


@article_bp.route("/<int:article_id>", methods=['GET'])
def get_article(article_id):
    """
    fetch article by id
    :param article_id:
    :return:
    """
    return jsonify(ArticleRepository(Session()).get_article_by_id(int(article_id)))