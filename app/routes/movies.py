from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models import Movie, Screening
from app import db

# 創建一個名為'movies'的 Blueprint
bp = Blueprint('movies', __name__)

# 定義一個名為'/movies'的路由，方法為POST，需要 JWT 認證
@bp.route('/movies', methods=['POST'])
@jwt_required
def create_movie():
    # 實現創建電影的邏輯
    pass

@bp.route('/movies', methods=['GET'])
def get_movies():
    # 實現獲取電影列表的邏輯
    pass

@bp.route('/movies/<int:id>', methods=['GET'])
def get_movie(id):
    # 實現獲取單個電影的邏輯
    pass

@bp.route('/movies/<int:id>/screenings', methods=['GET'])
def get_movie_screenings(id):
    # 實現獲取電影放映時間的邏輯
    pass