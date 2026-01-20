from flask import request

def get_user():
    return request.headers.get('X-Forwarded-User')
