from flask import Blueprint, jsonify

from server.db import Session
from server.repositories.techcrunch_repository import AuthorRepository

author_bp = Blueprint('author', __name__, url_prefix='/v1/authors')


@author_bp.route("/", methods=['GET'])
def get_authors():
    return jsonify(AuthorRepository(Session()).get_authors())


@author_bp.route("/v1/authors/<id>", methods=['GET'])
def get_author(author_id):
    return jsonify(AuthorRepository(Session()).get_author_by_id(int(author_id)))