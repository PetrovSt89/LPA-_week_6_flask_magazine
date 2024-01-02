import requests

from webapp.magazine.models import News, Comment
from webapp.db import db

def get_data(url, params=None):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }
    try:
        result = requests.get(url, params=params, headers=headers)
        return result.text
    except (requests.RequestException, ValueError):
        print('Сетевая ошибка')
        return False
    

def save_news(title, url, published, text=None):
    news_exists = News.query.filter(News.url == url).count()
    if not news_exists:
        news_news = News(title=title, url=url, published=published, text=text)
        db.session.add(news_news)
        db.session.commit()


def save_comment(text, news_id, user_id, created=None):
    comment = Comment(text=text, news_id=news_id, user_id=user_id, created=created)
    db.session.add(comment)
    db.session.commit()