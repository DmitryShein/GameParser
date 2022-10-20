import requests
from bs4 import BeautifulSoup as BS
import csv

URL="https://stopgame.ru/games/filter?rating=izumitelno"
HOST="https://stopgame.ru" #We need that to get true link (We get HOST + href (link))

#get html by request
def get_html(url):
    return requests.get(url)

#get content from html page
def get_content(html):
    html = BS(html.content, 'html.parser')
    #We take block with the games
    items = html.find_all('div', class_='item game-summary game-summary-horiz')

    for item in items:
        games.append(
            {
                'title':item.find('div', class_='caption caption-bold').get_text().replace("\n", "").strip(),
                'rating':item.find('div', class_='score').get_text().replace("\n", "").replace(" ",""),
                'link':HOST + item.find('a').get('href')
            }
        )
    return games
def print_games(games):
    for game in games:
        print(game)
    print('Count parsed games: ', len(games))

#def write_to_csv(games):

games = []

#for main page
html_request = get_html(URL)
games.append(get_content(html_request))
print("parsed page: 1")

for page in range(18):
    last_of_link = '&p='+str(page+2)
    url = URL+last_of_link
    html_request = get_html(url)
    games.append(get_content(html_request))
    print("parsed page:", page+2)

print_games(games)


