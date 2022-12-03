""" Sever side of all views catagorized as general views """
from flask import Blueprint, render_template, redirect, url_for


views = Blueprint('views', __name__)

@views.route('/')
def home(): 
    return redirect(url_for('auth.logIn'))

@views.route('/joy-is-arrived/')
def celebrate():
    return render_template('celebration.html')