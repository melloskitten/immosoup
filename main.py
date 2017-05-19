import random
import sys
import time

# Custom Classes
import telebot
from auxiliary import flatten
from webcrawler import LinkManager

# Page URLs with 'cheap' appartments
page_url_immoscout = 'https://www.immobilienscout24.de/Suche/S-2/Wohnung-Miete/Bayern/Muenchen/-/-/-/EURO--800,00'
prefix_url_immoscout = "https://www.immobilienscout24.de"
page_url_immonet = 'https://www.immonet.de/immobiliensuche/sel.do?&sortby=0&suchart=1&objecttype=1&marketingtype=2&parentcat=1&toprice=800&city=121673&locationname=M%C3%BCnchen'
prefix_url_immonet = "https://www.immonet.de"

# Grab Bot Key & init Telebot
BOT_KEY = sys.argv[1]
bot = telebot.TelegramBot(BOT_KEY)

# Init vars
appartment_links = []

# Initialize Bot and start timer for timeout reminder
start = time.time()

while True:

    bot.print_status()

    if bot.has_timeout(start):
        start = time.time()

    bot.update_subscribers()

    immoscout = LinkManager(page_url_immoscout, prefix_url_immoscout, {"class": "result-list-entry__brand-title-container"})
    immonet = LinkManager(page_url_immonet, prefix_url_immonet, {"class": "block ellipsis text-225"})

    app_urls = immoscout.links + immonet.links
    flatten(app_urls)

    for link in app_urls:
        if not link in appartment_links:
            appartment_links.append(link)
            bot.send_messages(link)

    time.sleep(180 + (random.randint(0, 9) * 10))
