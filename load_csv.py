import sys
import csv
from app import db, models

reload(sys)
sys.setdefaultencoding('utf8')

file = sys.argv[1]
category_name = sys.argv[2]

with open(file, 'rb') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        article = models.Article(
            key=unicode(row['Key'], errors='replace'),
            item_type=unicode(row['Item Type'], errors='replace'),
            publication_year=unicode(row['Publication Year'], errors='replace'),
            author=unicode(row['Author'], errors='replace'),
            title=unicode(row['Title'], errors='replace'),
            publication_title=unicode(row['Publication Title'], errors='replace'),
            isbn=unicode(row['ISBN'], errors='replace'),
            issn=unicode(row['ISSN'], errors='replace'),
            doi=unicode(row['DOI'], errors='replace'),
            url=unicode(row['Url'], errors='replace'),
            abstract_note=unicode(row['Abstract Note'], errors='replace'),
            date=unicode(row['Date'], errors='replace'),
            date_added=unicode(row['Date Added'], errors='replace'),
            date_modified=unicode(row['Date Modified'], errors='replace'),
            access_date=unicode(row['Access Date'], errors='replace'),
            pages=unicode(row['Pages'], errors='replace'),
            num_pages=unicode(row['Num Pages'], errors='replace'),
            issue=unicode(row['Issue'], errors='replace'),
            volume=unicode(row['Volume'], errors='replace'),
            num_volumes=unicode(row['Number Of Volumes'], errors='replace'),
            journal_abbreviation=unicode(row['Journal Abbreviation'], errors='replace'),
            short_title=unicode(row['Short Title'], errors='replace'),
            series=unicode(row['Series'], errors='replace'),
            series_number =unicode(row['Series Number'], errors='replace'),
            series_text =unicode(row['Series Text'], errors='replace'),
            series_title =unicode(row['Series Title'], errors='replace'),
            publisher =unicode(row['Publisher'], errors='replace'),
            place =unicode(row['Place'], errors='replace'),
            language =unicode(row['Language'], errors='replace'),
            rights =unicode(row['Rights'], errors='replace'),
            type =unicode(row['Type'], errors='replace'),
            archive =unicode(row['Archive'], errors='replace'),
            archive_location =unicode(row['Archive Location'], errors='replace'),
            library_catalog =unicode(row['Library Catalog'], errors='replace'),
            call_number =unicode(row['Call Number'], errors='replace'),
            extra =unicode(row['Extra'], errors='replace'),
            notes =unicode(row['Notes'], errors='replace'),
            file_attachments =unicode(row['File Attachments'], errors='replace'),
            link_attachments =unicode(row['Link Attachments'], errors='replace'),
            manual_tags =unicode(row['Manual Tags'], errors='replace'),
            auto_tags =unicode(row['Automatic Tags'], errors='replace'),
            category = unicode(category_name)
        )
        db.session.merge(article)
    db.session.commit()
    db.session.close()
    articles = models.Article.query.all()
    for article in articles:
        print article.key