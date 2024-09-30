from flask import Blueprint, request, jsonify

from app.models import User  
from app import db  

# 創建一個名為'auth'的 Blueprint    
bp = Blueprint('auth', __name__)

# 定義一個名為'/register'的路由，方法為POST
@bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()

    print("Incoming data:", data)

    # 如果數據為空，返回錯誤信息
    if data is None:
        return jsonify({"error": "No data provided or data is not valid JSON"}), 400

    # 如果缺少必填字段，返回錯誤信息
    if 'username' not in data or 'email' not in data:
        return jsonify({"error": "Missing username or email"}), 400

    # 嘗試檢查用戶是否已經存在
    try:
        existing_user = User.query.filter_by(username=data['username']).first()
        if existing_user:
            return jsonify({"error": "Username already exists"}), 409

        # 創建一個新的用戶
        user = User(username=data['username'], email=data['email'])
        db.session.add(user)  
        db.session.commit()    

        return jsonify({"message": "User registered successfully!"}), 201

    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500
