from flask import Blueprint, render_template, request, redirect, url_for,flash, abort, session
from flask_login import login_required, current_user, login_fresh
from .models import Game, Question, User
from ._tools_ import updateSessionTime
from . import db

game = Blueprint('game', __name__)


@game.route("/game/")
def baseLandingForGame():
    updateSessionTime()
    if (current_user.is_authenticated):
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
@login_required
def loggedUserPlay():
    return render_template('gamePlay.html', user=current_user)


def onlyMe(template_name:str='questionsManager.html', **kwargs):
    if not current_user.is_authenticated:
        abort(401) # unauthorized
    elif current_user.isMe == True:
        return render_template(template_name, **kwargs)
    elif current_user.isMe != True:
        abort(403) # forbidden
    
@game.route("/question-manager/")
@login_required
def mng():
    return redirect(url_for('game.questionMng_Landing', user_alias=current_user.alias))

@game.route("/add/")
@login_required
def add():
    return redirect(url_for("game.questionMng_AddQ", user_alias=current_user.alias))

@game.route("/edit/")
@login_required
def edit():
    return redirect(url_for("game.questionMng_Query", user_alias=current_user.alias))

@game.route("/<string:user_alias>/have-fun-with-my-game/questions-management/", methods=['GET'])
@login_required
def questionMng_Landing(user_alias):
    return onlyMe(user=current_user) # auto render template
    
@game.route("/<string:user_alias>/have-fun-with-my-game/questions-management/query/", methods=['POST', "GET"])
@login_required
def questionMng_Query(user_alias):
    onlyMe(user=current_user) # just restrict the access
    if request.method == 'POST':
        id = request.form.get("new_question")
        question = Question.query.filter_by(q_id=id).first()
        session['question'] = question
        return redirect(url_for("game.questionMng_EditQ", user_alias=current_user.alias))
    return render_template('plain.html', user=current_user, query=True)

@game.route("/<string:user_alias>/have-fun-with-my-game/questions-management/add-question/", methods=['POST', "GET"])
@login_required
def questionMng_AddQ(user_alias):
    onlyMe(user=current_user) # just restrict the access
    if request.method == 'POST':
        new_question = request.form.get("new_question")
        answer = request.form.get('answer')
        question = Question()
        # try:
        #    db.session.add()
        #    db.session.commit()
        #    flash("Question has been added", category="success")
        # except:
        #   pass
        #
        
    return render_template('questionsManager.html', user=current_user, add=True)

@game.route("/<string:user_alias>/have-fun-with-my-game/questions-management/edit-question/", methods=['POST', "GET"])
@login_required
def questionMng_EditQ(user_alias):
    onlyMe(user=current_user) # just restrict the access
    if 'question' in session:
        if session['question'] == None:
            return redirect(url_for('game.add'))
    elif not 'question' in session:
        return redirect(url_for('game.add'))
    if request.method == 'POST':
        question = session['question']
        new_question = request.form.get("new_question")
        answer = request.form.get('answer')
        toBeEdited = question
        session['question'] = None # clear the question data
    return render_template('questionsManager.html', user=current_user, edit=True)