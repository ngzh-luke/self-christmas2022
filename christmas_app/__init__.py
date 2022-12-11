# Root file of the system
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import PendingRollbackError
from flask_bcrypt import Bcrypt, generate_password_hash
from flask_login import LoginManager, current_user
from flask import Flask, Blueprint, render_template, abort, flash
from decouple import config as en_var # import the environment var

db = SQLAlchemy()
DB_NAME = "christmas_app2022_database.sqlite"

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

    from .views import views
    from .authen import auth
    from .features import features
    from .accountMng import account
    # from .views.dashboard_user import user_dashboard
    app.register_blueprint(rootView, url_prefix='/')
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    app.register_blueprint(features, url_prefix='/')
    app.register_blueprint(account, url_prefix='/')

    with app.app_context(): # Drop all of the tables
        db.drop_all()

    with app.app_context():
        db.create_all()

    from .models import User
    @app.before_first_request
    def demo_account():
        try:

            d1 = User(fname="ADMIN", alias="admin", password=generate_password_hash("admin").decode('utf-8'))
            
            db.session.add(d1)
            db.session.commit()
       
        except Exception as e:
            db.session.rollback()
            flash(f'{e}', category='error')

    from .accounts import create_accounts
    @app.before_first_request
    def accounters():
        try:
            a = create_accounts()
            db.session.add_all(a)
            db.session.commit()
        
        except Exception as e:
            db.session.rollback()
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

    def __str__(self) -> str:
        return str("{ " + f"Version: {self.version} | Status: {self.status} | Build: {self.build} | Updates: {self.version_note}" + " }")

    def getSystemVersion(self) -> str:
        return str(self.version)
    
 
    def getSystemAboutInfo() -> str :
        return "Details appear here..."

systemInfoObject = About(version=0.3221, status='Initial Development#6.1',
                         build=20221211, version_note='minor overall improvements')
systemInfo = systemInfoObject.__str__()
systemVersion = systemInfoObject.getSystemVersion()

rootView = Blueprint('rootView', __name__)
@rootView.route("/..root-template-view/")
def root_view():
    return render_template("root.html", about=systemInfo, user=current_user)

# - Initial Development#6.1: minor overall improvements on December 11, 2022 -> **0.3221**