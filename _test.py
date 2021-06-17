import os
import pymongo
import pytest
if os.path.exists("env.py"):
    import env


def test_vars_exist():
    envs = [
        "IP",
        "PORT",
        "SECRET_KEY",
        "MONGO_URI",
        "MONGO_DBNAME",
        "MEADE_PASS",
        "EMAIL_LOGIN",
        "EMAIL_PASS"]
    if os.path.exists("env.py"):
        for x in envs:
            assert os.getenv(x) is not None, \
                "Please set environment variable '{}'".format(x)
    else:
        assert os.path.exists("env.py"), "Create an env.py file"


