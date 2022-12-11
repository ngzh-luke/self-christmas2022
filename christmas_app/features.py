from flask import Blueprint, render_template, request, redirect, url_for,flash
from flask_login import login_required, current_user
# from ._tools_ import flash  # import customized flash method (flask)
from .models import User


features = Blueprint('features', __name__)

def checker(nextLoc:str="") -> None:
    if request.method == "POST":
        account_ = request.form.get('account_').upper()
        if account_ is not None:
            user = User.query.filter_by(fname=account_).first()
            if user is not None:
                user_fname = user.fname
                if user_fname == account_:
                    flash('You may use your first name to login.', category='found')
            
            else:
                flash("However, you still can enjoy the present without logged in ^_^", category='not found')
        else:
                flash("However, you still can enjoy the present without logged in ^_^", category='not found')


@features.route("/<string:user_alias>/cake/")
@login_required
def cake(user_alias):
    return render_template('cake.html', user=current_user)


@features.route('/check-account/by-first-name/', methods=['POST'])
def independantChecker():
    checker('/login')
    return redirect(url_for('features.independantCheckerLanding'))

@features.route('/check-account/', methods=['GET'])
def independantCheckerLanding():
    return render_template('checker.html', user=current_user)       


@features.route("/game/")
def baseLandingForGame():
    try:
        if User.get_id(current_user):
            return redirect(url_for("game.loggedUser_gameLanding", user_alias=current_user.alias)) # redirect to logged in user game
    except:
        pass
    return redirect(url_for('game.guestUser_gameLanding'))