# backend/init_db.py

from app import create_app
from models.database import db, User

def init_database():
    """初始化数据库并创建管理员账号"""
    app = create_app()
    
    with app.app_context():
        # 创建所有表
        db.create_all()
        print("✓ 数据库表创建成功！")
        
        # 检查是否已有管理员
        admin = User.query.filter_by(role='admin').first()
        
        if not admin:
            # 创建默认管理员账号
            admin = User(
                username='admin',
                role='admin'
            )
            admin.set_password('admin123')  # 默认密码
            
            db.session.add(admin)
            db.session.commit()
            
            print("✓ 默认管理员账号创建成功！")
            print("  用户名: admin")
            print("  密码: admin123")
            print("  ⚠️  请登录后立即修改密码！")
        else:
            print("✓ 管理员账号已存在")

if __name__ == '__main__':
    init_database()
