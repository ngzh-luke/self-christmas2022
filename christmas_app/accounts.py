""" Used to pre-defined user accounts """
from flask import flash
from flask_bcrypt import generate_password_hash
from .models import User

def create_dad():
    dad = None
    try:
        dad = User(fname='AARON',password=generate_password_hash('09-21').decode('utf-8'), alias='Dad')
    except:
        flash("Couldn't add more row to database", category='danger')
    return dad

def create_mom():
    mom = None
    try:
        mom = User(fname='SARAH',password=generate_password_hash('08-07').decode('utf-8'), alias='Mom')
    except:
        flash("Couldn't add more row to database", category='danger')
    return mom

def create_pa():
    pa = None
    try:
        pa = User(fname='CHATCHAI',password=generate_password_hash('06-28').decode('utf-8'), alias='Pa')
    except:
        flash("Couldn't add more row to database", category='danger')
    return pa

def create_mama():
    mama = None
    try:
        mama = User(fname='BHORNRAPEE',password=generate_password_hash('08-06').decode('utf-8'), alias='Mama')
    except:
        flash("Couldn't add more row to database", category='danger')
    return mama

def create_me():
    me = None
    try:
        me = User(fname='KITTIPICH',password=generate_password_hash('superKan').decode('utf-8'), alias='Kan')
    except:
        flash("Couldn't add more row to database", category='danger')
    return me

def create_accounts():
    pa = create_pa()
    ma = create_mama()
    dad = create_dad()
    mom = create_mom()
    me = create_me()
    return [me, pa, ma, dad, mom]