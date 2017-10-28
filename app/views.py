from app import app
from app import db, models

from flask import render_template, redirect, abort, url_for, jsonify

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/ishar-library/')
def ishar_library():
    return render_template('ISHARLibrary.html')
