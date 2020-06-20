from flask import Flask
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail, Message
from config import Config


app = Flask(__name__)
app.config.from_object(Config)

app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'prova@gmail.com'
app.config['MAIL_PASSWORD'] = 'prova12'

db = SQLAlchemy(app)
ma = Marshmallow(app)
mail = Mail(app)


from app import routes, models
