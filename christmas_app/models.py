# Database schema
import datetime
import time

from flask_login import UserMixin, current_user

from . import db


class User(db.Model, UserMixin):
    """ Database table: user
        each user account setting/properties defined here.
        
        #Attribute:
            fname -> first name,
            alias -> alias (not null),
            password -> password,
            points -> foreign key to Game table
        """
    id = db.Column(db.Integer(), unique=True, primary_key=True)
    fname = db.Column(db.String(56)) # first name
    alias = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String())
    points = db.relationship('Game')


    def __str__(self):
        return self.fname

    @property
    def isMe(self) -> bool:
        if not current_user.is_authenticated:
            # return current_app.login_manager.unauthorized()
            return False
        elif current_user.is_authenticated and (current_user.fname == 'KITTIPICH') :
            return True
        return False



class Game(db.Model):
    """ Database table: game
        each time that player plays game the information and result properties defined here
        """
    id = db.Column(db.Integer(), primary_key=True)
    start_time = db.Column(db.DateTime())
    finish_time = db.Column(db.DateTime())
    score = db.Column(db.Integer(), nullable=False, default=0)
    counter = db.Column(db.Integer(), nullable=False, default=0)
    played_by = db.Column(db.String(), db.ForeignKey('user.fname'), nullable=False)


    def __str__(self) -> str:
        return str("ID: " + self.id + " Finished at: " + self.finish_time)

    def __init__(self, start_at:datetime.datetime, finish_at:datetime.datetime, score:int, c:int):
        def increment() -> int:
            current = self.counter
            increased = current + 1
            self.counter = increased
            return self.counter
        self.start_time = start_at
        self.finish_time = finish_at
        self.score = score
        self.counter = increment()



class Question(db.Model):
    """ Database table: question
        each question that will ask users
        """
    q_id = db.Column(db.Integer(), nullable=False, primary_key=True) # question id
    q = db.Column(db.String(), nullable=False) # question
    a = db.Column(db.String(), nullable=True) # answer