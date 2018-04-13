from functools import wraps

from flask import request, jsonify
from flask_restful import abort
from itsdangerous import (TimedJSONWebSignatureSerializer as Serializer)

SECRET_KEY = "A RANDOM KEY"


def authenticate_by_token(token):
    if token is None:
        return False
    s = Serializer(SECRET_KEY)
    try:
        username = s.loads(token.encode())
        if username == 'admin':
            return True
    except:
        return False

    return False


def login_required(f, message="You are not authorized"):
    @wraps(f)
    def decorated_function(*args, **kwargs):

        token = request.headers.get("AUTH_TOKEN")
        if authenticate_by_token(token):
            return f(*args, **kwargs)

        return jsonify(message=message), 401
        # abort(401, message=message)

    return decorated_function
