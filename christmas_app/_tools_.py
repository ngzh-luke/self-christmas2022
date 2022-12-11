""" Customized function(s) used in the system"""


from flask.signals import message_flashed
from flask.globals import current_app
#from flask.signals import _signals
from flask import session
import typing as t
# my_signals = _signals

# model_saved = my_signals.signal('flashed')


# # customize flash function without overriding the default flash one
# def flash(message: str, category: str = "message",*args: t.Any, **kwargs: t.Any) -> None:
#     """Flashes a message to the next request.  In order to remove the
#     flashed message from the session and to display it to the user,
#     the template has to call :func:`get_flashed_messages`.

#     .. versionchanged:: 0.3
#        `category` parameter added.

#     :param message: the message to be flashed.
#     :param category: the category for the message.  The following values
#                      are recommended: ``'message'`` for any kind of message,
#                      ``'error'`` for errors, ``'info'`` for information
#                      messages and ``'warning'`` for warnings.  However any
#                      kind of string can be used as category.
    
#     :param [any]: any
#     """
#     # Original implementation:
#     #
#     #     session.setdefault('_flashes', []).append((category, message))
#     #
#     # This assumed that changes made to mutable structures in the session are
#     # always in sync with the session object, which is not true for session
#     # implementations that use external storage for keeping their keys/values.
#     flashes = session.get("_flashes", [])
#     flashes.append((category, message))
#     session["_flashes"] = flashes
#     message_flashed.send(
#         current_app._get_current_object(),  # type: ignore
#         message=message,
#         category=category
        
#     )


# def isDone() -> bool:
    