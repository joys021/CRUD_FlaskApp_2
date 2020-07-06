# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 14:54:55 2020
Initialize our Flask app
Then import db object and initialise it
@author: joy
"""
import os
from flask import Flask
from flask import jsonify
from api.utils.database import db # import db object
from api.utils.responses import response_with
import api.utils.responses as resp
from api.routes.authors import author_routes
from api.routes.books import book_routes
from flask_jwt_extended import JWTManager
from api.routes.users import user_routes
from api.utils.email import mail


app = Flask(__name__)

if os.environ.get('WORK_ENV') == 'PROD':
    app_config = ProductionConfig
elif os.environ.get('WORK_ENV') == 'TEST':
    app_config = TestingConfig
else:
    app_config = DevelopmentConfig
    
app.config.from_object(app_config)

#initialize JWTManager
jwt = JWTManager(app)
mail.init_app(app)
db.init_app(app)
with app.app_context():
    db.create_all()

# START GLOBAL HTTP CONFIGURATIONS
app.register_blueprint(author_routes, url_prefix='/api/authors')
app.register_blueprint(book_routes, url_prefix='/api/books')
app.register_blueprint(user_routes, url_prefix='/api/users')


@app.route('/avatar/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],filename)

@app.after_request
def add_header(response):
    return response
    
@app.errorhandler(400)
def bad_request(e):
    logging.error(e)
    return response_with(resp.BAD_REQUEST_400)
    
@app.errorhandler(500)
def server_error(e):
    logging.error(e)
    return response_with(resp.SERVER_ERROR_500)
    
@app.errorhandler(404)
def not_found(e):
    logging.error(e)
    return response_with(resp. SERVER_ERROR_404)
    
    
db.init_app(app)
with app.app_context():
    db.create_all()


'''
#initialise db object
def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)
    db.init_app(app)
    with app.app_context():
        db.create_all()
    return app
   
'''   

if __name__ == "__main__":
    app.run(port=5000, host="0.0.0.0", use_reloader=False)