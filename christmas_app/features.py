from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user
from ._tools_ import flash
from .models import User
from .authen import checker # import pre-defined account checker method

features = Blueprint('features', __name__)

@features.route("/<string:user_alias>/cake/")
@login_required
def cake(user_alias):
    return render_template('cake.html', user=current_user)


# def checker(value) -> None:
#     if request.method == "POST":

        
#         user = User.query.filter_by(fname=value).first()
#         if user is not None:
            
#             flash('You may use your first name to login.', category='found')
            
#         else:
#             flash("However, you still can enjoy the present without logged in ^_^", category='not found')


# @features.route(f"/check-account/by-first-name/?value=" + "<string:user_fname>", methods=["POST", "GET"])
# def independantChecker(user_fname):
    
#     checker(user_fname)
#     return render_template('checker.html', user=current_user)

@features.route('/check-account/by-first-name/', methods=['GET','POST'])
def independantCheckerLanding():
    checker()
    return render_template('checker.html', user=current_user)
    