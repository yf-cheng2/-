# backend/config.py

import os
from datetime import timedelta

class Config:
    # 基础配置
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key-change-in-production'
    
    # 数据库配置
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'mysql+pymysql://root:123456@localhost:3306/road_damage'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # JWT配置
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY') or 'jwt-secret-key'
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=24)
    
    # 上传文件配置
    UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), 'uploads')
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
    
    # 模型配置
    MODEL_PATH = os.path.join(os.path.dirname(__file__), 'models', 'best.pt')
    
    # 病害类型映射
    DISEASE_TYPES = {
        0: 'longitudinal_crack',  # 纵向裂缝
        1: 'transverse_crack',     # 横向裂缝
        2: 'alligator_crack',      # 鳄鱼裂缝
        3: 'pothole'               # 坑洞
    }
