# immosoup
Immoscout24 crawler for receiving Telegram notifications on new affordable appartments in Munich, using BeautifulSoup. 

# How To:

1. You can adjust your appartment query by changing `page_url_immoscout` and `page_url_immonet` (in `main.py`) according to your needs. We recommend to sort the immobilienscout24 and immonet pages by 'Newest Entries First'. 

2. Grab a telegram bot ID. A tutorial for that can be found [here](https://docs.microsoft.com/en-us/azure/bot-service/bot-service-channel-connect-telegram?view=azure-bot-service-4.0). Make sure to grab the `BOT_ID`.

3. Run the script via: `python main.py [BOT_ID]`

# Authors
- [johannesrohwer](https://github.com/johannesrohwer)
- [melloskitten](https://github.com/melloskitten)
