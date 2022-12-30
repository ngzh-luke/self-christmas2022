""" Sever side of all views catagorized as customized views """
from flask import Blueprint, render_template, redirect, url_for, session, flash
from flask_login import current_user, login_required
from .models import User
from ._tools_ import updateSessionTime

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
                flash('Redirected to general view (likely because you do not have customized for you view)', category='info')
                return redirect(url_for('views.celebrate', user=current_user, user_alias=current_user.alias))
    except:
        pass
    return redirect(url_for('views.celebrate', user=current_user, user_alias=current_user.alias))

@cusViews.route('/for/admin/customized-celebration-view/') # test view
@cusViews.route("/for/Kan/customized-celebration-view/") # self (can't click the quick link button to access the page due to the redirect function)
@login_required
def admin():
    session['current'] = '/customized-view/'
    return "Customized for admin (Kan)"

@cusViews.route("/for/Dad/customized-celebration-view/") # dad
@login_required
def dad():
    session['current'] = '/customized-view/'
    if current_user.alias != 'Dad':
        alias = current_user.alias
        alias = alias.lower()
        try:
            return redirect(url_for("cViews."+alias))
        except:
            return redirect(url_for('cViews.redirector'))
    return render_template("dad.html", user=current_user, title='just for Dad ^_^')

@cusViews.route("/for/Mom/customized-celebration-view/") # mom
@login_required
def mom():
    session['current'] = '/customized-view/'
    if current_user.alias != 'Mom':
        alias = current_user.alias
        alias = alias.lower()
        try:
            return redirect(url_for("cViews."+alias))
        except:
            return redirect(url_for('cViews.redirector'))
    return render_template("mom.html", user=current_user)

@cusViews.route("/for/Pa/customized-celebration-view/") # pa
@login_required
def pa():
    session['current'] = '/customized-view/'
    if current_user.alias != 'Pa':
        alias = current_user.alias
        alias = alias.lower()
        try:
            return redirect(url_for("cViews."+alias))
        except:
            return redirect(url_for('cViews.redirector'))
    return render_template("pa.html", user=current_user)

@cusViews.route("/for/Mama/customized-celebration-view/") # mama
@login_required
def mama():
    session['current'] = '/customized-view/'
    if current_user.alias != 'Mama':
        alias = current_user.alias
        alias = alias.lower()
        try:
            return redirect(url_for("cViews."+alias))
        except:
            return redirect(url_for('cViews.redirector'))
    return render_template("ma.html", user=current_user)

@cusViews.route("/for/Addy/customized-celebration-view/") # addy
@login_required
def addy():
    session['current'] = '/customized-view/'
    if current_user.alias != 'Addy':
        alias = current_user.alias
        alias = alias.lower()
        try:
            return redirect(url_for("cViews."+alias))
        except:
            return redirect(url_for('cViews.redirector'))
    return render_template("addy.html", user=current_user)

@cusViews.route("/for/Evander/customized-celebration-view/") # evander
@login_required
def evander():
    session['current'] = '/customized-view/'
    if current_user.alias != 'Evander':
        alias = current_user.alias
        alias = alias.lower()
        try:
            return redirect(url_for("cViews."+alias))
        except:
            return redirect(url_for('cViews.redirector'))
    return render_template("evander.html", user=current_user)

@cusViews.route("/for/AjTrithep/customized-celebration-view/") # aj.trithep 
@login_required
def ajtrithep():
    session['current'] = '/customized-view/'
    if current_user.alias != 'AjTrithep':
        alias = current_user.alias
        alias = alias.lower()
        try:
            return redirect(url_for("cViews."+alias))
        except:
            return redirect(url_for('cViews.redirector'))
    return render_template("ajTrithep_ajJade.html", user=current_user)

@cusViews.route("/for/AjJade/customized-celebration-view/") # aj.jade
def ajjade():
    session['current'] = '/customized-view/'
    if current_user.alias != 'AjJade':
        alias = current_user.alias
        alias = alias.lower()
        try:
            return redirect(url_for("cViews."+alias))
        except:
            return redirect(url_for('cViews.redirector'))
    return render_template("ajTrithep_ajJade.html", user=current_user)

@cusViews.route("/for/Papa/customized-celebration-view/") # papa
def papa():
    session['current'] = '/customized-view/'
    if current_user.alias != 'Papa':
        alias = current_user.alias
        alias = alias.lower()
        try:
            return redirect(url_for("cViews."+alias))
        except:
            return redirect(url_for('cViews.redirector'))
    return render_template("grandma_papa.html", user=current_user)

@cusViews.route("/for/Grandma/customized-celebration-view/") # grandma
def grandma():
    session['current'] = '/customized-view/'
    if current_user.alias != 'Grandma':
        alias = current_user.alias
        alias = alias.lower()
        try:
            return redirect(url_for("cViews."+alias))
        except:
            return redirect(url_for('cViews.redirector'))
    return render_template("grandma_papa.html", user=current_user)


@cusViews.route("/for/Kwan/customized-celebration-view/") # kwan
def kwan():
    session['current'] = '/customized-view/'
    if current_user.alias != 'Kwan':
        alias = current_user.alias
        alias = alias.lower()
        try:
            return redirect(url_for("cViews."+alias))
        except:
            return redirect(url_for('cViews.redirector'))
    return render_template("kwan.html", user=current_user)

@cusViews.route("/for/Wish/customized-celebration-view/") # wish
def wish():
    session['current'] = '/customized-view/'
    if current_user.alias != 'Wish':
        alias = current_user.alias
        alias = alias.lower()
        try:
            return redirect(url_for("cViews."+alias))
        except:
            return redirect(url_for('cViews.redirector'))
    return render_template("wish.html", user=current_user)

@cusViews.route("/for/Noemi/customized-celebration-view/") # noemi
def noemi():
    session['current'] = '/customized-view/'
    if current_user.alias != 'Noemi':
        alias = current_user.alias
        alias = alias.lower()
        try:
            return redirect(url_for("cViews."+alias))
        except:
            return redirect(url_for('cViews.redirector'))
    return render_template("noemi.html", user=current_user)

@cusViews.route("/for/Anna/customized-celebration-view/") # anna
def anna():
    session['current'] = '/customized-view/'
    if current_user.alias != 'Anna':
        alias = current_user.alias
        alias = alias.lower()
        try:
            return redirect(url_for("cViews."+alias))
        except:
            return redirect(url_for('cViews.redirector'))
    return render_template("anna.html", user=current_user)

@cusViews.route("/for/Candice/customized-celebration-view/") # candice
def candice():
    session['current'] = '/customized-view/'
    if current_user.alias != 'Candice':
        alias = current_user.alias
        alias = alias.lower()
        try:
            return redirect(url_for("cViews."+alias))
        except:
            return redirect(url_for('cViews.redirector'))
    return render_template("candice.html", user=current_user)