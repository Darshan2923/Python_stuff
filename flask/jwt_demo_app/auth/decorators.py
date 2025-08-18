from functools import wraps
from flask import request,jsonify
from .utils import decode_token

def jwt_required(func):
    @wraps(func)
    def decorated(*args, **kwargs):
        auth_header=request.headers.get('Authorization',None)
        if not auth_header or not auth_header.startswith('Bearer '):
            return jsonify({"error": "Missing or invalid token"}), 401

        token = auth_header.split(" ")[1]
        payload = decode_token(token)
        if not payload:
            return jsonify({"error": "Invalid or expired token"}), 401

        # Optionally, you can attach the user information to the request
        request.user = payload["sub"]

        return func(*args, **kwargs)
    return decorated