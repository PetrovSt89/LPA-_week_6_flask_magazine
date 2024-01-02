import datetime
from webapp.db import db
from webapp.magazine.models import News


def parse_news():
        title = 'Скоро ехать за Дашей'
        url = None
        published = datetime.datetime.now()
        insert_news(title=title, url=url, published=published)

def insert_news(title, url, published):
    news_exists = News.query.filter(News.url == url).count()
    if not news_exists:
        news = News(title=title, url=url, published=published)
        db.session.add(news)
        db.session.commit()