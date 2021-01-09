import os

from flask import Flask
from flask import url_for, redirect, render_template, send_from_directory, request

app = Flask(__name__)
app.config['DEBUG'] = True


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')







if __name__ == '__main__':
    app.run()
