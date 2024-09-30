from flask import Blueprint, request, jsonify 
from flask_jwt_extended import create_access_token  
from app.models import User  
from app import db  

auth_bp = Blueprint('auth_bp', __name__)  # 創建一個名為'auth_bp'的Blueprint

# 定義一個名為'register'的路由，方法為POST
@auth_bp.route('/register', methods=['POST'])  
def register():
    data = request.get_json()  # 從請求中獲取JSON數據
    if not data:
        return jsonify({'error': 'No data provided'}), 400  
    
    username = data.get('username')  
    email = data.get('email')  
    password = data.get('password')  
    
    if not username or not email or not password:
        return jsonify({'error': 'Username, email, and password are required'}), 400  # 如果任何一個必填字段為空，返回錯誤信息
    
    if User.query.filter_by(username=username).first():
        return jsonify({'error': 'Username already exists'}), 400  # 如果用戶名已經存在，返回錯誤信息
    
    if User.query.filter_by(email=email).first():
        return jsonify({'error': 'Email already exists'}), 400  # 如果email已經存在，返回錯誤信息
    
    try:
        user = User(username=username, email=email)  # 創建一個新的用戶
        user.set_password(password)  
        db.session.add(user)  
        db.session.commit()  
        return jsonify({'message': 'User registered successfully'}), 201  # 返回成功信息
    except Exception as e:
        db.session.rollback()  # 如果發生錯誤，回滾會話
        return jsonify({'error': 'An error occurred while registering the user', 'details': str(e)}), 500  # 返回錯誤信息

@auth_bp.route('/login', methods=['POST'])  # 定義一個名為'login'的路由，方法為POST
def login():
    data = request.get_json()  # 從請求中獲取JSON數據
    if not data:
        return jsonify({'error': 'No data provided'}), 400  # 如果數據為空，返回錯誤信息
    
    username = data.get('username')  
    password = data.get('password')  
    
    if not username or not password:
        return jsonify({'error': 'Username and password are required'}), 400  # 如果任何一個必填字段為空，返回錯誤信息
    
    user = User.query.filter_by(username=username).first()  
    if user and user.check_password(password):
        access_token = create_access_token(identity=user.id)  
        return jsonify({'access_token': access_token}), 200  
    return jsonify({'message': 'Invalid username or password'}), 401  # 如果用戶名或密碼無效，返回錯誤信息