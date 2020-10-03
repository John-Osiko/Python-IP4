from flask import Flask 
from config import Config
from flask_mail import Mail
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_uploads import IMAGES, UploadSet,configure_uploads

db = SQLAlchemy()
mail = Mail()
bootstrap = Bootstrap()
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'
photos = UploadSet('photos',IMAGES)



def create_app():
    app = Flask(__name__)
    
    
    # Creating the app configurations
    app.config.from_object(Config)


    # Initializing flask extensions
    bootstrap.init_app(app)
    # Initialized application
    db.init_app(app)
    # Initialized login manager
    login_manager.init_app(app)
    # Initialized flask mail
    mail.init_app(app)

    from .auth import auth as auth_blueprint
    from .main import main as main_blueprint

    # Will add authentication views
    app.register_blueprint(auth_blueprint)
    # Will add the views and forms
    app.register_blueprint(main_blueprint)

    return app