# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 15:37:34 2020
defines the basic config that did in main.py and
then adds environment-specific configuration on the top

@author: joy
"""


class Config(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = <Production DB URL>
    SECRET_KEY= 'secured_key_here'
    SECURITY_PASSWORD_SALT= 'security_password_here'
    
class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = <Development DB URL>
    SQLALCHEMY_ECHO = False
    SECRET_KEY= 'secured_key_here'
    SECURITY_PASSWORD_SALT= 'security_password_here'
    
class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_ECHO = False
    JWT_SECRET_KEY = 'JWT-SECRET'
    SECRET_KEY= 'SECRET-KEY'
    SECURITY_PASSWORD_SALT= 'PASSWORD-SALT'
    MAIL_DEFAULT_SENDER= ''
    MAIL_SERVER= 'smtp.gmail.com'
    MAIL_PORT= 465
    MAIL_USERNAME= ""
    MAIL_PASSWORD= ""
    MAIL_USE_TLS= False
    MAIL_USE_SSL= True
    UPLOAD_FOLDER= 'images'
    
    
#configure flask-mail
MAIL_DEFAULT_SENDER= 'email_address'
MAIL_SERVER= 'email_providers_smtp_address'
MAIL_PORT= <mail_server_port>
MAIL_USERNAME= 'your_email_address'
MAIL_PASSWORD= 'your_email_password'
MAIL_USE_TLS= False
MAIL_USE_SSL= True
UPLOAD_FOLDER= 'images'
    