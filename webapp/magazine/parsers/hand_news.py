import datetime
from webapp.magazine.parsers.utils import save_news, save_comment

def hand_create_news():
        title = 'Мама тоже собирает елку'
        url = None
        published = datetime.datetime.now()
        text = 'у нас теперь две елки, большая и маленькая'
        date_str = '21 дек 2023 13:35'
        published = datetime.datetime.strptime(date_str, '%d %b %Y %H:%M')
        save_news(title=title, url=url, published=published, text=text)

def hand_create_comments():
        text = 'елочка гори'
        news_id = 4
        user_id = 1
        save_comment(text=text, news_id=news_id, user_id=user_id)