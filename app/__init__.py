import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_wtf.csrf import CSRFProtect
from .config import Config

app = Flask(__name__)
csrf = CSRFProtect(app)
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

app.config['UPLOAD_FOLDER'] = os.path.join(os.getcwd(), 'uploads')

from app import views