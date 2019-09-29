# flask_blog/__init__.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object('flask_blog.config')

db = SQLAlchemy(app)


from flask_blog.views.entries import entry  # NOQA
app.register_blueprint(entry, url_prefix='/useers')


from flask_blog.views import views  # NOQA
