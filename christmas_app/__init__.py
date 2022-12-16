# Root file of the system
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import PendingRollbackError
from flask_bcrypt import Bcrypt, generate_password_hash
from flask_login import LoginManager, current_user
from flask import Flask, Blueprint, render_template, abort, flash, session
from flask.sessions import SessionInterface, SessionMixin
from decouple import config as en_var # import the environment var
from datetime import timedelta, datetime, timezone
from time import strftime, strptime
db = SQLAlchemy()
DB_NAME = "christmas_app2022_database.sqlite"
TIMEOUT = timedelta(hours=1)

def create_app():
    app = Flask(__name__)
    f_bcrypt = Bcrypt()
    app.config['FLASK_ADMIN-SWATCH'] = 'cerulean'
    app.config['SECRET_KEY'] = en_var('christmas_app2022') # Encrepted with Environment Variable
    app.config['DATABASE_NAME'] = DB_NAME
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['REMEMBER_COOKIE_SECURE'] = True
    app.config['PERMANENT_SESSION_LIFETIME'] = TIMEOUT # set session timeout (need to use with before_request() below)
    # app.config[''] 
    app.config['TIMEZONE'] = 'Asia/Bangkok'
    
    f_bcrypt.init_app(app)
    db.init_app(app)

    from .views import views
    from .authen import auth
    from .features import features
    from .accountMng import account
    from .game import game
    from ._ss_ import acc_security
    app.register_blueprint(rootView, url_prefix='/')
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    app.register_blueprint(features, url_prefix='/')
    app.register_blueprint(account, url_prefix='/')
    app.register_blueprint(game, url_prefix='/')
    app.register_blueprint(acc_security, url_prefix='/@system-@security-check')

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

    # config the user session
    @app.before_request
    def before_request():
        session.permanent = True
        # session.modified = True # default set to true. Consult the lib to confirm

    login_manager = LoginManager()
    login_manager.login_view = 'auth.logIn'
    login_manager.refresh_view = 'auth.logIn'
    login_manager.login_message_category = 'info'
    login_manager.needs_refresh_message_category = "info"
    login_manager.needs_refresh_message = "You have to login again to confirm your identity!"
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app
""" 
    @app.after_request
    # Virtually check the session. the system session is seperated
    def checkSessionTime(response): # must return a response
        timeLeft = None
        end = datetime.now(tz=timezone.utc)
        if ("loginTime" in session and 'timeoutTime' in session):
            start = session['loginTime']
            timeSpent = end - start
            if (session['lastActiveTime'] > start):
                lastActiveTime = session['lastActiveTime']
            else:
                lastActiveTime = start
            timeLeft = session['timeoutTime'] - lastActiveTime
            session['timeLeft'] = str(timeLeft)
            flash(f'You have spent {timeSpent} for current session and have {timeLeft} until the session ends', category='info')
        return response 
    """
    #return app

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

systemInfoObject = About(version=0.452, status='Initial Development#8.1',
                         build=20221216, version_note='account security check enhancement, bugs fixed, and overall improvements')
systemInfo = systemInfoObject.__str__()
systemVersion = systemInfoObject.getSystemVersion()

rootView = Blueprint('rootView', __name__)
@rootView.route("/..root-template-view/")
def root_view():
    if not current_user.is_authenticated:
        abort(401)
    elif current_user.isMe == True:
        return render_template("root.html", about=systemInfo, user=current_user)
    else:
        abort(403)

# - Initial Development#8.1: account security check enhancement, bugs fixed, and overall improvements on December 16, 2022 -> **0.452**