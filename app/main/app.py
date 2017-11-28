# -*- coding: utf-8 -*-
"""Example NumPy style docstrings.

"""
import os
from flask import Flask, render_template

# https://stackoverflow.com/questions/31002890/how-to-reference-a-html-template-from-a-different-directory-in-python-flask
path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..',
                                    'templates'))

app = Flask(__name__, template_folder=path)


@app.route('/')
def hello_world():
    return '<h1>Hello World!</h1>'


@app.route('/upload')
def upload_video():
    return render_template('upload_video.html')


if __name__ == '__main__':
    app.run(debug=True)
