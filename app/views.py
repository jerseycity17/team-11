from app import app, db, models

from flask import render_template, redirect, abort, url_for, jsonify

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/ishar-library/')
def ishar_library():
    return render_template('ISHARLibrary.html')

@app.route('/ishar-JournalPortal/')
def ishar_journal_portal():
    return render_template('ISHARJournalPortal.html')
