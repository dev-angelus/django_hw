#pip install requests/beautifulsoup4
import requests
from bs4 import BeautifulSoup as bs
from django.views.decorators.csrf import csrf_exempt

URL = 'http://www.manascinema.com'
URL2 = 'https://cinematica.kg'

HEADERS = {
    'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.2 Safari/605.1.15",
}

#start
@csrf_exempt
def get_html(url, params=''):
    req = requests.get(url, headers=HEADERS, params=params)
    return req

#get data
@csrf_exempt
def get_data(html):
    soup = bs(html, "html.parser")
    items = soup.find_all('div', class_='short_movie_info')

    cinema_kg = []

    for item in items:
        cinema_kg.append(
            {
                'title_name': item.find('div', class_='m_title').get_text(),
                'title_url': URL + item.find('a').get('href'),
                'image': URL + item.find('div', class_='m_thumb').find('img').get('src'),
            }
        )
    return cinema_kg

@csrf_exempt
def get_data2(html2):
    soup2 = bs(html2, "html.parser")
    items2 = soup2.find_all('a', class_='movie-dummy')
    cinema_kg1 = []

    for item2 in items2:
        cinema_kg1.append(
            {
                'title_name': item2.find('div', class_='movie-title').get_text(),
                'title_url': URL2 + item2.find('a').get('href'),
                'image': URL2 + item2.find('div', class_='movie-poster').find('img').get('src'),
            }
        )
    return cinema_kg1

#endparse
@csrf_exempt
def parser():
    html = get_html(URL)
    if html.status_code == 200:
        cinema_kg2 = []
        for page in range(0, 1):
            html = get_html(f'http://www.manascinema.com/movies', params=page)
            cinema_kg2.extend(get_data(html.text))
        return cinema_kg2
    else:
        raise Exception('Error in parser!')


@csrf_exempt
def parser2():
    html2 = get_html(URL2)
    if html2.status_code == 200:
        cinema_kg3 = []
        for pages2 in range(0, 1):
            html2 = get_html(f'https://cinematica.kg/movies', params=pages2)
            cinema_kg3.extend(get_data2(html2.text))
        return cinema_kg3
    else:
        raise Exception('Error in parser!')

