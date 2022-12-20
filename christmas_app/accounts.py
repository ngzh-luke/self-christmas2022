""" Used to pre-defined user accounts """
from flask import flash
from flask_bcrypt import generate_password_hash
from .models import User
from decouple import config as en_var # import the environment var

usernames = {en_var('name_dad'):en_var('pass_dad'),en_var('name_mom'):en_var('pass_mom'),en_var('name_pa'):en_var('pass_pa'),en_var('name_mama'):en_var('pass_mama'),en_var('name_self'):en_var('pass_self') \
    ,"ADMIN":"admin"}

def create_dad():
    dad = None
    try:
        dad = User(fname=en_var('name_dad'),password=generate_password_hash(usernames[en_var('name_dad')]).decode('utf-8'), alias='Dad')
    except:
        flash("Couldn't add more row to database", category='danger')
    return dad

def create_mom():
    mom = None
    try:
        mom = User(fname=en_var('name_mom'),password=generate_password_hash(usernames[en_var('name_mom')]).decode('utf-8'), alias='Mom')
    except:
        flash("Couldn't add more row to database", category='danger')
    return mom

def create_pa():
    pa = None
    try:
        pa = User(fname=en_var('name_pa'),password=generate_password_hash(usernames[en_var('name_pa')]).decode('utf-8'), alias='Pa')
    except:
        flash("Couldn't add more row to database", category='danger')
    return pa

def create_mama():
    mama = None
    try:
        mama = User(fname=en_var('name_mama'),password=generate_password_hash(usernames[en_var('name_mama')]).decode('utf-8'), alias='Mama')
    except:
        flash("Couldn't add more row to database", category='danger')
    return mama

def create_me():
    me = None
    try:
        me = User(fname=en_var('name_self'),password=generate_password_hash(usernames[en_var('name_self')]).decode('utf-8'), alias='Kan')
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