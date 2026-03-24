# backend/app.py
from flask import send_from_directory
from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from config import Config
from models.database import db

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    # 初始化扩展
    db.init_app(app)
    CORS(app)
    JWTManager(app)

    # 在 create_app() 中 app 初始化完成后添加：
    @app.route('/uploads/<path:filename>')
    def uploaded_file(filename):
        return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

    # 创建上传文件夹
    import os
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    
    # 注册蓝图（后面创建）
    from routes.auth import auth_bp
    from routes.users import users_bp
    from routes.detection import detection_bp
    from routes.tasks import tasks_bp
    
    app.register_blueprint(auth_bp, url_prefix='/api/auth')
    app.register_blueprint(users_bp, url_prefix='/api/users')
    app.register_blueprint(detection_bp, url_prefix='/api/detection')
    app.register_blueprint(tasks_bp, url_prefix='/api/tasks')
    
    return app

if __name__ == '__main__':
    app = create_app()
    
    with app.app_context():
        db.create_all()  # 创建数据库表
        print("数据库表创建成功！")
    
    app.run(debug=True, host='0.0.0.0', port=5000)
