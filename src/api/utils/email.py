# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 18:53:26 2020

@author: joy
"""


from flask_mail import Message,Mail
from flask import current_app
mail = Mail()


def send_email(to, subject, template):
    msg = Message(subject,recipients=[to],html=template,sender=current_app.config['MAIL_DEFAULT_SENDER'])
    mail.send(msg)