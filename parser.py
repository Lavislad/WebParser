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
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    print(soup)
    products = soup.find_all('div', attrs={'class': '_2rw4E _2g7lE'})
    print(products)
    for i in products:
        title = i.find('span', class_='ds-text ds-text_lineClamp_2 ds-text_weight_med ds-text_color_text-primary ds-text_typography_lead-text ds-text_lead-text_normal ds-text_lead-text_med ds-text_lineClamp').get_text()
        price = i.find('span', class_='cds-text ds-text_weight_bold ds-text_color_price-sale ds-text_typography_headline-5 ds-text_headline-5_tight ds-text_headline-5_bold').get_text()
        link = i.fint('a', attrs={'class': 'EQlfk'}).get_text()
        result[f'{i}'].append(f'Product {i}')
        result[f'{i}'][f'Product {i}'].append(f'Title: {title}')
        result[f'{i}'][f'Product {i}'].append(f'Price: {price}')
        result[f'{i}'][f'Product {i}'].append(f'link: {link}')
    return result

print(parser('https://market.yandex.ru/search?text=universal%20audio%20volt%201&hid=91027&rs=eJwz0gpgrGLhmHyc9RMjBweDBIMCkPmXkQEIeplA5FQwuYIJKAwA3HAJWg%2C%2C&rt=9'))