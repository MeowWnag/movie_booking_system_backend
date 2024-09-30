from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from app.config import Config
import logging
from logging.handlers import RotatingFileHandler

db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # 初始化擴展
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    CORS(app)  # 如果需要，啟用CORS

    # 設置日誌
    if not app.debug:
        handler = RotatingFileHandler('error.log', maxBytes=10240, backupCount=10)
        handler.setLevel(logging.INFO)
        app.logger.addHandler(handler)

    # 註冊藍圖
    from app.routes import movies, reservations, reports  # 先匯入其他模組
    from app.routes import auth  # 單獨匯入 auth，避免循環匯入
    app.register_blueprint(auth.auth_bp)  # 確保使用正確的 Blueprint 名稱

    return app
