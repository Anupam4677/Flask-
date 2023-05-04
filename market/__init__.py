# import flask instance from flask package 
from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy

# initialize the instace of the flask with given argument __name__
# # app = Flask(__name__)
# # app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
# # db = SQLAlchemy(app)

# with app.app_context():
#     db.create_all()
# app.app_context().push()

# def create_app():
#     with app.app_context():
#         db.create_all()


from market import routes