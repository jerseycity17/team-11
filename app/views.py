from app import app
from app import db, models

from flask import render_template, redirect, abort, url_for, jsonify, request
from sqlalchemy import or_, not_

from collections import OrderedDict

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
    pagination = models.Article.query.filter(or_(
        models.Article.auto_tags.contains(tag),
        models.Article.manual_tags.contains(tag)
    )).paginate(per_page=10)
    return render_template('articles_with_tag.html', tag=tag, pagination=pagination, articles=pagination.items)
    
@app.route('/categories/<category>/', methods=['GET'])
def view_articles_with_category(category):
    pagination = models.Article.query.filter_by(category=category).paginate(per_page=10)
    return render_template('articles_with_category.html', category=category, pagination=pagination, articles=pagination.items)
    
@app.route('/tags/', methods=['GET'])
def view_tags():
    tags_list = [article.auto_tags for article in models.Article.query.all()]
    tag_dict = {}
    for tags in tags_list:
        tag_list = tags.split(';')
        for tag in tag_list:
            if tag not in tag_dict:
                tag_dict[tag] = 1
            else:
                tag_dict[tag] += 1
    
    tags = OrderedDict(sorted(tag_dict.items(), key = lambda k: k[0]))
    
    return render_template('tags.html', tags=tags)
    
@app.route('/search/', methods=['GET'])
def search():
    value = request.args.get('val')
    search_results = []
    articles = []
    # normal search
    if value:
        search_results = models.Article.query.filter(or_(
            models.Article.abstract_note.contains(value),
            models.Article.title.contains(value),
            models.Article.author.contains(value),
            models.Article.category.contains(value),
            models.Article.auto_tags.contains(value),
            models.Article.manual_tags.contains(value),
            models.Article.publication_title.contains(value)
        )).order_by(models.Article.date_added.desc()).paginate(per_page=10)
        articles = search_results.items
    # advanced search
    else:
        search_results = models.Article.query
        searched = False
        if request.args.get('title_search'):
            searched = True
            title = request.args.get('title_search')
            if request.args.get('title_search_filter') == '1':
                search_results = search_results.filter(models.Article.title.contains(title))
            else:
                search_results = search_results.filter(not_(models.Article.title.contains(title)))
        if request.args.get('author_search'):
            searched = True
            author = request.args.get('author_search')
            if request.args.get('author_search_filter') == '1':
                search_results = search_results.filter(models.Article.author.contains(author))
            else:
                search_results = search_results.filter(not_(models.Article.author.contains(author)))
        if request.args.get('abtract_search'):
            searched = True 
            abtract = request.args.get('abtract_search')
            if request.args.get('abtract_search_filter') == '1':
                search_results = search_results.filter(models.Article.abtract_note.contains(abtract))
            else:
                search_results = search_results.filter(not_(models.Article.abtract_note.contains(abtract)))
        if request.args.get('publication_title_search'):
            searched = True
            publication_title = request.args.get('publication_title_search')
            if request.args.get('publication_title_search_filter') == '1':
                search_results = search_results.filter(models.Article.publication_title.contains(publication_title))
            else:
                search_results = search_results.filter(not_(models.Article.publication_title.contains(publication_title)))
        if request.args.get('tag_search'):
            searched = True
            tags = request.args.get('tag_search').split(',')
            if request.args.get('tag_search_filter') == '1':
                for tag in tags:
                    search_results = search_results.filter(or_(models.Article.auto_tags.contains(tag),(models.Article.manual_tags.contains(tag))))
            else:
                for tag in tags:
                    search_results = search_results.filter(not_(or_(models.Article.auto_tags.contains(tag),(models.Article.manual_tags.contains(tag)))))
                    
        if request.args.get('category_search'):
            searched = True
            category = request.args.get('category_search')
            if request.args.get('category_search_filter') == '1':
                search_results = search_results.filter(models.Article.category.contains(category))
            else:
                search_results = search_results.filter(not_(models.Article.category.contains(category)))
        if searched:
            search_results = search_results.paginate(per_page=10)
            articles = search_results.items
        else:
            search_results = []
            articles = []
    return render_template('search.html', pagination=search_results, articles=articles, value=value, **request.args.to_dict())