import requests
from bs4 import BeautifulSoup

def parser(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    news_elem = soup.find('div', class_='elem')
    title = news_elem.find('h3').get_text()
    date = news_elem.find('h4', class_='date')
    full_text = news_elem.find('p')
    return title

print(parser('https://vlados.akeka.ru/news/'))