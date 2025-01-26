import requests
from bs4 import BeautifulSoup as BS

URL = 'https://books.yandex.ru/'

HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
}

#1

def get_html(url, params=''):
    request = requests.get(url, headers=HEADERS, params=params)
    return request

#2

def get_data(html):
    bs = BS(html, features='html.parser')
    books = bs.find_all('div', class_='ContentPreview_container__aBjig')
    book_list = []
    for book in books:
        title = book.find('div', class_='ContentPreview_info__UdqJi').get_text()
        img = book.find("img").get('src')
        book_list.append(
            {
                'title':title,
                'img': img
            }
        )
        
    return book_list

#3

def parsing():
    response = get_html(URL)
    if response.status_code == 200:
        book_list2 = []
        for page in range(1,2):
            response = get_html(f'https://books.yandex.ru/', params={'page':page})
            book_list2.extend(get_data(response.text))
            return book_list2
        else:
            raise Exception('Error in parsing')
        
# print(parsing())