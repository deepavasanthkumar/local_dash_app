from flask import abort
from auth.sso import get_user

def authorize():
    if not get_user(): abort(401)
