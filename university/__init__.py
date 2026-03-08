from flask import Flask
from flask_wtf.csrf import CSRFProtect

csrf = CSRFProtect()

def create_app():
    app = Flask(__name__)
    
    # Настройки
    app.config['SECRET_KEY'] = 'development-key'
    app.config['DEBUG'] = True
    app.config['WTF_CSRF_ENABLED'] = True  # Включить CSRF защиту
    
    # Инициализируем CSRF защиту
    csrf.init_app(app)
    
    # Регистрируем Blueprint
    from .routes import bp
    app.register_blueprint(bp)
    
    return app