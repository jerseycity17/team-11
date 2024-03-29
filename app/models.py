from app import db

class Article(db.Model):
    key = db.Column(db.String, primary_key=True)
    item_type = db.Column(db.String, index=True)
    publication_year = db.Column(db.String, index=True)
    author = db.Column(db.String, index=True)
    title = db.Column(db.String, index=True)
    publication_title = db.Column(db.String, index=True)
    isbn = db.Column(db.String, index=True)
    issn = db.Column(db.String, index=True)
    doi = db.Column(db.String, index=True)
    url = db.Column(db.String, index=True)
    abstract_note = db.Column(db.String, index=True)
    date = db.Column(db.String, index=True)
    date_added = db.Column(db.String, index=True)
    date_modified = db.Column(db.String, index=True)
    access_date = db.Column(db.String, index=True)
    pages = db.Column(db.String, index=True)
    num_pages = db.Column(db.String, index=True)
    issue = db.Column(db.String, index=True)
    volume = db.Column(db.String, index=True)
    num_volumes = db.Column(db.String, index=True)
    abstract = db.Column(db.String, index=True)
    journal_abbreviation = db.Column(db.String, index=True)
    short_title = db.Column(db.String, index=True)
    series = db.Column(db.String, index=True)
    series_number = db.Column(db.String, index=True)
    series_text = db.Column(db.String, index=True)
    series_title = db.Column(db.String, index=True)
    publisher = db.Column(db.String, index=True)
    place = db.Column(db.String, index=True)
    language = db.Column(db.String, index=True)
    rights = db.Column(db.String, index=True)
    type = db.Column(db.String, index=True)
    archive = db.Column(db.String, index=True)
    archive_location = db.Column(db.String, index=True)
    library_catalog = db.Column(db.String, index=True)
    call_number = db.Column(db.String, index=True)
    extra = db.Column(db.String, index=True)
    notes = db.Column(db.String, index=True)
    file_attachments = db.Column(db.String, index=True)
    link_attachments = db.Column(db.String, index=True)
    manual_tags = db.Column(db.String, index=True)
    auto_tags = db.Column(db.String, index=True)
    category = db.Column(db.String, index=True)