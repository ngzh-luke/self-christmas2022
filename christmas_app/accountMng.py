from flask import redirect, render_template, Blueprint
from flask_login import current_user, login_required

account = Blueprint('acc', __name__)

@account.route('/<string:user_alias>/account-management/')
@login_required
def manager(user_alias):
    return render_template('account.html', user=current_user)