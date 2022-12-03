# Root file of the system
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt, generate_password_hash
from flask_login import LoginManager, current_user
from flask import Flask, Blueprint, render_template, abort, flash
from .models import User
from decouple import config as en_var # import the environment var

DB_NAME = "christmas_app2022_database.sqlite"
db = SQLAlchemy()
def create_app():
    app = Flask(__name__)
    f_bcrypt = Bcrypt()
    app.config['FLASK_ADMIN-SWATCH'] = 'cerulean'
    app.config['SECRET_KEY'] = en_var('christmas_app2022') # Encrepted with Environment Variable
    app.config['DATABASE_NAME'] = DB_NAME
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['TIMEZONE'] = 'Asia/Bangkok'
    
    f_bcrypt.init_app(app)
    db.init_app(app)

    # from .views.general import views
    # from .views.authen import auth
    # from .views.dashboard_admin import admin_dashboard
    # from .views.dashboard_user import user_dashboard
    # app.register_blueprint(rootView, url_prefix='/')
    # app.register_blueprint(views, url_prefix='/')
    # app.register_blueprint(auth, url_prefix='/')
    # app.register_blueprint(admin_dashboard, url_prefix='/')
    # app.register_blueprint(user_dashboard, url_prefix='/')

    with app.app_context(): # Drop all of the tables
        db.drop_all()

    with app.app_context():
        db.create_all()


    @app.before_first_request
    def demo_account():
        try:

            d1 = User(email="demo@admin.com", fname="Admin", lname="Admin Lastname", password=generate_password_hash("admin").decode('utf-8'),
             role_level=1, s_question='question', s_answer='answer')
            
            d2 = User(email='demo@user.com',fname="User", lname="User Lastname", 
            password=generate_password_hash("user").decode('utf-8'),s_question='question', 
            s_answer='answer')    
            
            db.session.add_all([d1, d2])
            db.session.commit()
        except Exception as e:
            flash(f'{e}', category='error')
            

    login_manager = LoginManager()
    login_manager.login_view = 'auth.logIn'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))



    return app

class About():
    version = float()
    status = str()
    build = int()
    version_note = str()

    def __init__(self, version: float = float(0.0), status: str = 'None Stated', build: int = 20221100, version_note: str = "None Stated"):
        self.version = version
        self.status = status
        self.build = build
        self.version_note = version_note

    def __repr__(self) -> str:
        return str("{ " + f"Version: {self.version} | Status: {self.status} | Build: {self.build} | Details: {self.version_note}" + " }")

    def getSystemVersion(self) -> str:
        return str(self.version)

systemInfoObject = About(version=0.2, status='Initial Development#2',
                         build=20221204, version_note='database schema implemented and initial developed')
systemInfo = systemInfoObject.__repr__()
systemVersion = systemInfoObject.getSystemVersion()

rootView = Blueprint('rootView', __name__)
@rootView.route("/..root-template-view/")
def root_view():
    return render_template("root.html", about=systemInfo, user=current_user)

# Initial Development#2: database schema implemented and initial developed on December 4, 2022 -> **0.2**