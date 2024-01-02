from datetime import datetime, timedelta
import locale
import platform

from bs4 import BeautifulSoup

from webapp.magazine.parsers.utils import get_data, save_news

from webapp.db import db
from webapp.magazine.models import News


if platform.system() == 'Windows':
    locale.setlocale(locale.LC_ALL, "russian")
else:
    locale.setlocale(locale.LC_TIME, 'ru_RU')


def parse_habr_date(date_str):
    if 'сегодня' in date_str:
        today = datetime.now()
        date_str = date_str.replace('сегодня', today.strftime('%d %B %Y'))
    elif 'вчера' in date_str:
        yesterday = datetime.now() - timedelta(days=1)
        date_str = date_str.replace('вчера', yesterday.strftime('%d %B %Y'))
    try:
        return datetime.strptime(date_str, '%d %b %Y %H:%M')
    except ValueError:
        return datetime.now()


def get_habr_snippets():
    html = get_data(
        url='https://habr.com/ru/search/?target_type=posts&q=python&order_by=date'
        )
    if html:
        soup = BeautifulSoup(html, 'html.parser')
        title = soup.find('a', class_="tm-title__link").text
        url = soup.find('a', class_="tm-title__link")['href']
        url = f'https://habr.com/{url}'
        published = soup.find('a','tm-article-datetime-published').text
        dt = published.split('в')[0].strip()
        t = published.split('в')[1].strip()
        if len(dt.split()) < 3:
            published = f'{dt} 2023 {t}'
        else:
            published = f'{dt} {t}'
        published = published.split()
        str_published = ''
        for i in range(len(published)):
            if i != len(published) - 1:
                str_published += published[i].strip() + ' '
            else:
                str_published += published[i].strip()
        published = parse_habr_date(str_published)
        save_news(title=title, url=url, published=published)


def get_news_content():
    news_without_text = News.query.filter(News.text.is_(None)).order_by(News.url.is_not(None))
    for news in news_without_text:
        html = get_data(news.url)
        if html:
            soup = BeautifulSoup(html, 'html.parser')
            news_text = soup.find('div', class_='tm-article-body')
            if news_text:
                print(news_text)
            else:
                print("нету ничего")
            # тут не доделал запись в базу данных, сраный хабр не выходит запарсить
