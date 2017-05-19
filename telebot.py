import telepot
import time

# Telegram Bot class
class TelegramBot:
    def __init__(self, KEY):
        self.bot = telepot.Bot(KEY)
        self.subscriber_list = set()
        self.scan_counter = 0

    def update_subscribers(self):
        response = self.bot.getUpdates()
        for el in response:
            self.subscriber_list.add(el['message']['chat']['id'])

    def send_messages(self, msg):
        for id in self.subscriber_list:
            self.bot.sendMessage(id, msg)

    def has_timeout(self, start):
        cur = time.time()
        if (cur - start) > 21000:
            self.send_messages("Please send me a message, so I can continue sending you super cool offers on appartments.")
            return True

    def print_status(self):
        print("New Scan... {}".format(self.scan_counter))
        self.scan_counter += 1