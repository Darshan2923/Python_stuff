from flask import Blueprint, jsonify, request
from auth.decorators import jwt_required

market_bp = Blueprint("market", __name__, url_prefix="/market")

@market_bp.route("/", methods=["GET"])
@jwt_required
def market_home():
    return jsonify({
        "message": f"Welcome to the Market, {request.user}!"
    })
