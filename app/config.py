import os
from dotenv import load_dotenv

load_dotenv()

class Config(object):
    """Base Config Object"""
    DEBUG = True
    SECRET_KEY = "HGLASH"
    MAIL_SERVER = "sandbox.smtp.mailtrap.io"
    MAIL_PORT = 465
    MAIL_USERNAME = "e472089ebc9894"
    MAIL_PASSWORD = "c9448aff64ec39"