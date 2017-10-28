from app import app
from app import db, models

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

@app.route('/content/<article_key>/', methods=['GET'])
def view_article(article_key):
    article = models.Article.query.filter_by(key=article_key).first()
    
    return render_template('article.html', article=article)
    
@app.route('/tags/<tag>/', methods=['GET'])
def view_articles_with_tag(tag):
    articles = ' '
    articles = models.Article.query.filter(models.Article.auto_tags.contains(tag)).all()
    articles += models.Article.query.filter(models.Article.manual_tags.contains(tag)).all()
    return render_template('articles_with_tag.html', tag=tag, articles=articles)