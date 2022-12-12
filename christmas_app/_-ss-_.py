""" Security and setting """
from flask import redirect
from flask_login import set_login_view, fresh_login_required, login_required
from ._tools_ import updateSessionTime