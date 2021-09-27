import logging
import re
import requests
import sys
from config import PUSHOVER_API_TOKEN, PUSHOVER_USER_KEY
from pushover_complete import PushoverAPI


logging.basicConfig(level=logging.INFO)

target = "https://pulsedmedia.com/clients/widgets/productsinfo.php?pid=241&get=price&billingcycle=monthly" # V1000 Auction 1TB
url_page = "https://pulsedmedia.com/seedbox-auctions.php"
PRICE_TARGET = 4.65

def getDocument(url):
    try:
        r = requests.get(url=target)
        return r.text

    except Exception as e:
        logging.error(e)
        sys.exit()

def grabPrice(doc):
    number = re.search(r"\d\.\d{2}", doc)
    return float(number.group(0))

def checkPriceUnder(price, price_target=PRICE_TARGET):
    if price < price_target:
        return True
    else:
        return False

def notifyPushover(current_price):
    pushover = PushoverAPI(PUSHOVER_API_TOKEN)
    pushover.send_message(PUSHOVER_USER_KEY,
                          "Current price is {}".format(current_price),
                          url=url_page,
                          url_title="Buy seedbox now!"
                    )

def main():
    document = getDocument(target)

    price = grabPrice(document)

    if checkPriceUnder(price):
        notifyPushover(price)
    else:
        logging.info("not a good price: {} > {}".format(price, PRICE_TARGET))

if __name__ == '__main__':
    main()
