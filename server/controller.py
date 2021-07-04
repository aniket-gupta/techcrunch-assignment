from flask import jsonify

from server import app
from server.db import Session
from server.repositories.techcrunch_repository import ArticleRepository, AuthorRepository


# @server.route("/v1/authors", methods=['GET'])
# def get_authors():
#     return jsonify(AuthorRepository(Session()).get_authors())
#
#
# @server.route("/v1/authors/<id>", methods=['GET'])
# def get_author(author_id):
#     return jsonify(AuthorRepository(Session()).get_author_by_id(int(author_id)))
#
#
# @server.route("/v1/articles", methods=['GET'])
# def get_articles():
#     return jsonify(ArticleRepository(Session()).get_articles())
#
#
# @server.route("/v1/articles/<id>", methods=['GET'])
# def get_article(article_id):
#     return jsonify(ArticleRepository(Session()).get_article_by_id(int(article_id)))



