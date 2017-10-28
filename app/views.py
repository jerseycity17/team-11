from app import app

from flask import render_template, redirect, abort, url_for, jsonify

@app.route('/')
def index():
    return render_template('index.html')