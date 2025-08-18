from flask import Blueprint,request,jsonify,make_response
from .utils import create_access_token, create_refresh_token, decode_token
import datetime

auth_bp=Blueprint('auth',__name__,url_prefix='/auth')

TEST_USER={
    "username": "admin",
    "password": "123456"
}

@auth_bp.route('/login', methods=['POST'])
def login():
    data=request.get_json()
    if not data:
        return jsonify({"error": "Missing credentials"}), 400
    
    username = data.get('username')
    password = data.get('password')

    if username != TEST_USER["username"] or password != TEST_USER["password"]:
        return jsonify({"error": "Invalid credentials"}), 401

    access_token = create_access_token(identity=username)
    refresh_token = create_refresh_token(identity=username)

    resp = make_response(jsonify({
        "access_token": access_token,
        "refresh_token": refresh_token
    }))

    resp.set_cookie("access_token", access_token, httponly=True, samesite="Strict")
    resp.set_cookie("refresh_token", refresh_token, httponly=True, samesite="Strict")

    return resp


@auth_bp.route("/refresh", methods=["POST"])
def refresh():
    refresh_token = request.cookies.get("refresh_token") or request.json.get("refresh_token")
    if not refresh_token:
        return jsonify({"error": "Missing refresh token"}), 401

    payload = decode_token(refresh_token)
    if not payload:
        return jsonify({"error": "Invalid or expired refresh token"}), 401

    username = payload["sub"]
    new_access = create_access_token(username)

    resp = make_response(jsonify({"access_token": new_access}))
    resp.set_cookie("access_token", new_access, httponly=True, samesite="Strict")

    return resp

@auth_bp.route("/logout", methods=["POST"])
def logout():
    resp = make_response(jsonify({"message": "Logged out"}))
    resp.delete_cookie("access_token")
    resp.delete_cookie("refresh_token")
    return resp