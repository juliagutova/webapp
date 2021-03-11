import requests
from bs4 import BeautifulSoup

def get_html(url):
    try:
        result = requests.get(url) # При помощи requests берем данные из этого url
        result.raise_for_status() #обработка ошибок
        return result.text #если все хорошо, вовращаем result text
    except(requests.RequestException, ValueError): #обработка ошибок
        print("Сетевая ошибка")
        return False

def get_python_news():
    html = get_html("https://www.python.org/blogs/")
    if html:
        soup = BeautifulSoup(html, 'html.parser')
        all_news = soup.find('ul', class_='list-recent-posts').findAll('li')
        result_news = []
        for news in all_news:
            title = news.find('a').text # название новости
            url = news.find('a')['href'] # ссылка
            published = news.find('time').text # дата
            result_news.append({ # список словарей
                "title": title,
                "url": url,
                "published": published
            })
        return result_news
    return False

