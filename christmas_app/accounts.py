""" Used to pre-defined user accounts """
from flask import flash
from flask_bcrypt import generate_password_hash
from .models import User


usernames = {"AARON":"09-21","SARAH":"08-07","CHATCHAI":"06-28","BHORNRAPEE":"08-06","KITTIPICH":"superKan" \
    ,"ADMIN":"admin"}

def create_dad():
    dad = None
    try:
        dad = User(fname='AARON',password=generate_password_hash(usernames['AARON']).decode('utf-8'), alias='Dad')
    except:
        flash("Couldn't add more row to database", category='danger')
    return dad

def create_mom():
    mom = None
    try:
        mom = User(fname='SARAH',password=generate_password_hash(usernames['SARAH']).decode('utf-8'), alias='Mom')
    except:
        flash("Couldn't add more row to database", category='danger')
    return mom

def create_pa():
    pa = None
    try:
        pa = User(fname='CHATCHAI',password=generate_password_hash(usernames['CHATCHAI']).decode('utf-8'), alias='Pa')
    except:
        flash("Couldn't add more row to database", category='danger')
    return pa

def create_mama():
    mama = None
    try:
        mama = User(fname='BHORNRAPEE',password=generate_password_hash(usernames['BHORNRAPEE']).decode('utf-8'), alias='Mama')
    except:
        flash("Couldn't add more row to database", category='danger')
    return mama

def create_me():
    me = None
    try:
        me = User(fname='KITTIPICH',password=generate_password_hash(usernames['KITTIPICH']).decode('utf-8'), alias='Kan')
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