# coding: utf-8
from __future__ import (
    absolute_import,
    print_function,
    unicode_literals,
)
import datetime as dt
import logging
import uuid

import flask
import pytz
from werkzeug.exceptions import BadRequest

app = flask.Blueprint('prediction', __name__, url_prefix='/prediction')


def bad_request(reason: str):
    resp = flask.jsonify(reason=reason)  # type: flask.Response
    resp.status_code = 400
    return BadRequest(response=resp)


@app.route('/', methods=['GET'])
def index():

    return 'hello'
