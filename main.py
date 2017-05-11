import random
import sys

import telepot
import time
from bs4 import BeautifulSoup
import requests

appartment_links = []
counter = 0
subscriber_list = set()
page_url = 'https://www.immobilienscout24.de/Suche/S-2/Wohnung-Miete/Bayern/Muenchen/-/-/-/EURO--800,00'
BOT_KEY = sys.argv[1]

bot = telepot.Bot(BOT_KEY)
response = bot.getUpdates()

for el in response:
    subscriber_list.add(el['message']['chat']['id'])

while True:

    print("New Scan... {}".format(counter))
    counter = counter + 1

    webpage = requests.get(page_url)
    soup = BeautifulSoup(webpage.text, 'html.parser')
    app_urls = soup.find_all("a", {"class" : "result-list-entry__brand-title-container"})

    for app_url in app_urls:
        link = 'https://www.immobilienscout24.de/' + app_url.attrs['href']
        if not link in appartment_links:
            appartment_links.append(link)
            for id in subscriber_list:
                bot.sendMessage(id, link)

    time.sleep(180 + (random.randint(0, 9) * 10))

