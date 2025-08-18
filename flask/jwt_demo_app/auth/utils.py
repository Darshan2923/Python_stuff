import jwt
from datetime import datetime, timedelta
from flask import current_app

def create_access_token(identity,expires_in=15):
    """
        create short-lived access token.
    """
    payload={
        "sub": identity,
        "exp": datetime.utcnow() + timedelta(minutes=expires_in),
        "iat": datetime.utcnow()
    }
    return jwt.encode(payload, current_app.config["JWT_SECRET_KEY"], algorithm="HS256")

def create_refresh_token(identity, expires_in=60*24):
    """
    Create long-lived refresh token (default 1 day).
    """
    payload = {
        "sub": identity,
        "exp": datetime.utcnow() + timedelta(minutes=expires_in),
        "iat": datetime.utcnow()
    }
    return jwt.encode(payload, current_app.config["JWT_SECRET_KEY"], algorithm="HS256")


def decode_token(token):
    """
    Decode token and return payload or None if invalid/expired.
    """
    try:
        payload = jwt.decode(
            token,
            current_app.config["JWT_SECRET_KEY"],
            algorithms=["HS256"]
        )
        return payload
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None