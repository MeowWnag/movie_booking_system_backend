from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy

# 資料庫模型
db = SQLAlchemy()

# 用戶模型
class User(db.Model):
    __tablename__ = 'app_user'  # 明確指定資料表名稱
# 用戶ID
    id = db.Column(db.Integer, primary_key=True)
# 用戶名
    username = db.Column(db.String(64), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    role = db.Column(db.String(20), default='user')

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

# 電影模型
class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    poster_url = db.Column(db.String(200))
    genre = db.Column(db.String(50))

# 放映模型
class Screening(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    movie_id = db.Column(db.Integer, db.ForeignKey('movie.id'), nullable=False)
    start_time = db.Column(db.DateTime, nullable=False)
    end_time = db.Column(db.DateTime, nullable=False)
    theater_number = db.Column(db.Integer, nullable=False)

# 座位模型
class Seat(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    screening_id = db.Column(db.Integer, db.ForeignKey('screening.id'), nullable=False)
    row = db.Column(db.String(1), nullable=False)
    number = db.Column(db.Integer, nullable=False)
    is_reserved = db.Column(db.Boolean, default=False)

# 預訂模型
class Reservation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    screening_id = db.Column(db.Integer, db.ForeignKey('screening.id'), nullable=False)
    seat_id = db.Column(db.Integer, db.ForeignKey('seat.id'), nullable=False)
    reservation_time = db.Column(db.DateTime, nullable=False)