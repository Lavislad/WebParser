from itertools import count

import requests
from bs4 import BeautifulSoup

# def parser(url):
#     r = requests.get(url)
#     soup = BeautifulSoup(r.text, 'html.parser')
#     news_elem = soup.find('div', class_='elem')
#     title = news_elem.find('h3').get_text()
#     date = news_elem.find('h4', class_='date').get_text()
#     full_text = news_elem.find('p').get_text()
#     return [title, date, full_text]

def parser(url):
    result = {}
    count = 0
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    news = soup.find_all('div', attrs={'class': 'elem'})
    for index, item in enumerate(news):
        title = item.find('h3').get_text()
        date = item.find('h4', class_='date').get_text()
        full_text = item.find('p').get_text()
        count += 1
        result['Count'] = count
        result[f'News {index + 1}'] = {
            'Title': title,
            'Date': date,
            'Full_text': full_text,
        }
    return result

for i in range(parser('https://vlados.akeka.ru/news/').get('Count')):
    print(parser('https://vlados.akeka.ru/news/').get(f'News {i + 1}').get('Title'))
    print(parser('https://vlados.akeka.ru/news/').get(f'News {i + 1}').get('Date'))
    print(parser('https://vlados.akeka.ru/news/').get(f'News {i + 1}').get('Full_text'))
    print('\n')
