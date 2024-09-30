from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models import Reservation, Seat, Screening
from app import db

bp = Blueprint('reservations', __name__)

@bp.route('/reservations', methods=['POST'])
@jwt_required
def create_reservation():
    # 實現創建預訂的邏輯
    pass

@bp.route('/reservations', methods=['GET'])
@jwt_required
def get_user_reservations():
    # 實現獲取用戶預訂的邏輯
    pass

@bp.route('/reservations/<int:id>', methods=['DELETE'])
@jwt_required
def cancel_reservation(id):
    # 實現取消預訂的邏輯
    pass