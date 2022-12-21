""" Sever side of all views catagorized as customized views """
from flask import Blueprint, render_template, redirect, url_for, session, flash
from flask_login import current_user, login_required
from .models import User
from ._tools_ import updateSessionTime
import time

cusViews = Blueprint('cViews', __name__)

@cusViews.route('/customized-view/')
@login_required
def redirector():
    session['current'] = '/customized-view/'
    try:
        if User.get_id(current_user):
            alias = current_user.alias
            alias = alias.lower()
            try:
                return redirect(url_for("cViews."+alias))
            except:
                flash('Redirected to general view', category='info')
                return redirect(url_for('views.celebrate', user=current_user, user_alias=current_user.alias))
    except:
        pass
    return redirect(url_for('views.celebrate', user=current_user, user_alias=current_user.alias))

@cusViews.route('/for/admin/customized-celebration-view/') # test view
@login_required
def admin():
    return "Customized for admin"

@cusViews.route("/for/Dad/customized-celebration-view/") # dad
@login_required
def dad():
    if current_user.alias != 'Dad':
        alias = current_user.alias
        alias = alias.lower()
        try:
            flash("Redirected to customized for you view", category='info')
            return redirect(url_for("cViews."+alias))
        except:
            return redirect(url_for('cViews.redirector'))
    return render_template("dad.html", user=current_user)