from flask import (
    session
)

def check_login():
    if session.get("user"):
        return True
    else:
        return False