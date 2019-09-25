# flask_blog/views.py

from flask_blog import app


@app.route('/')
def show_entries():
    return "Hello World!"
