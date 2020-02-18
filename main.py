# coding=utf-8

import random
import sys
import time

# Custom Classes
import telebot
from auxiliary import flatten
from webcrawler import LinkManager

# Page URLs with 'cheap' appartments
page_url_immoscout = 'https://www.immobilienscout24.de/Suche/S-2/Wohnung-Miete/Bayern/Muenchen/-/2,00-/60,00-/EURO--1800,00/-/-/-/-/true'
prefix_url_immoscout = "https://www.immobilienscout24.de"
page_url_immonet = 'https://www.immonet.de/immobiliensuche/sel.do?fromarea=60.0&city=121673&parentcat=1&suchart=2&marketingtype=2&toprice=1800.0&fromrooms=2.0&radius=0&facilities=44&facilities=110&facilities=189&facilities=20&listsize=26&objecttype=1&pageoffset=1&sortby=19'
prefix_url_immonet = "https://www.immonet.de"

# Grab Bot Key & init Telebot
BOT_KEY = sys.argv[1]
bot = telebot.TelegramBot(BOT_KEY)

# Init vars
appartment_links = []

# Initialize Bot and start timer for timeout reminder
start = time.time()

while True:
    try:
        bot.print_status()
    
        if bot.has_timeout(start):
            start = time.time()
    
        bot.update_subscribers()
    
        immoscout = LinkManager(page_url_immoscout, prefix_url_immoscout, {"class": "result-list-entry__brand-title-container"})
        immonet = LinkManager(page_url_immonet, prefix_url_immonet, {"class": "block ellipsis text-225 text-default"})
    
        app_urls = immoscout.links + immonet.links
        flatten(app_urls)
    
        for link in app_urls:
            if not link in appartment_links:
                print("Found new: {}".format(link))
                appartment_links.append(link)
                bot.send_messages(link)
                time.sleep(3)

        time.sleep(180 + (random.randint(0, 9) * 10))

    except (KeyboardInterrupt, SystemExit):
        # Allow to terminate the script using CTRL-C
        raise
    except Exception as e:
        # Log exception and retry after a 60s delay
        print(e)
        time.sleep(60)
 
