import logging
import traceback

import sqlalchemy
from flask import Flask, jsonify

from sqlalchemy.exc import SQLAlchemyError

from server.exceptions import NotFound, BadRequest
from server.routes.article import article_bp
from server.routes.author import author_bp

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')

app = Flask(__name__)
app.config.from_object('config.Config')

app.register_blueprint(article_bp)
app.register_blueprint(author_bp)


@app.errorhandler(NotFound)
def handle_exception(err):
    """Handle resource not found error"""
    response = {"error": err.description}
    app.logger.error(f"{err.description}")
    return jsonify(response), err.code


@app.errorhandler(BadRequest)
def handle_exception(err):
    """Handle resource not found error"""
    response = {"error": err.description}
    app.logger.error(f"{err.description}")
    return jsonify(response), err.code


@app.errorhandler(SQLAlchemyError)
def handle_exception(err):
    """Handle DB connection errors """
    response = {
        "error": err.description,
    }
    if isinstance(err, sqlalchemy.exc.InternalError):
        response["error"] = "Unable to connect to DB"
    return jsonify(response), 500


@app.errorhandler(500)
def handle_exception(err):
    """Return JSON instead of HTML for any other server error"""
    app.logger.error(f"Unknown Exception: {str(err)}")
    app.logger.debug(''.join(traceback.format_exception(etype=type(err), value=err, tb=err.__traceback__)))
    response = {"error": "Sorry, that error is on us, please contact support if this wasn't an accident"}
    return jsonify(response), 500


