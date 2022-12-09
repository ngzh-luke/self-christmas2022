""" Sever side of all views catagorized as general views """
from flask import Blueprint, render_template, redirect, url_for
from christmas_app import systemInfoObject, About
from flask_login import current_user
from .models import User

views = Blueprint('views', __name__)

@views.route('/')
def landing(): 
    # try:
    #     if User.get_id(current_user):
    #         return redirect(url_for("features.c", user_id=current_user.fname)) # redirect to cake page
    # except:
    #     pass
    return render_template('landing.html', user=current_user)
    

@views.route('/joy-is-arrived/')
def celebrate():
    return render_template('celebration.html',user=current_user)

@views.route('/about/')
def about():
    return render_template('about.html', user=current_user, ab=systemInfoObject, info=About.getSystemAboutInfo())