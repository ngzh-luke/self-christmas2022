from flask import Blueprint, render_template, request, redirect, url_for,flash
from flask_login import login_required, current_user, login_fresh
from .models import Game, Question, User
from ._tools_ import updateSessionTime

game = Blueprint('game', __name__)


@game.route("/game/")
def baseLandingForGame():
    updateSessionTime()
    if (login_fresh is not True):
        return redirect(url_for("game.loggedUser_gameLanding", user_alias=current_user.alias)) # redirect to logged in user game
    else:
        return redirect(url_for('game.guestUser_gameLanding'))


@game.route('/<string:user_alias>/have-fun-with-my-game/')
@login_required
def loggedUser_gameLanding(user_alias):
    return render_template('gameLanding.html', user=current_user)

@game.route('/as-a-guest/have-fun-with-my-game/')
def guestUser_gameLanding():
    try:
        if User.get_id(current_user):
            return redirect(url_for("game.loggedUser_gameLanding", user_alias=current_user.alias))
    except:
        pass
    return render_template('gameLanding.html', user=current_user)

@game.route("/as-a-guest/have-fun-with-my-game/play/")
def guestUserPlay():
    return render_template('gamePlay.html', user=current_user)


@game.route("/<string:user_alias>/have-fun-with-my-game/play/")
def loggedUserPlay():
    return render_template('gamePlay.html', user=current_user)
