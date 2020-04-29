import requests
import app.constants
from bs4 import BeautifulSoup


class Offer:
    name: str = ''
    price: float = ''
    loyaltyLenght: int = ''
    priceFeatures: str = ''
    dataPacket: str = ''
    sms: str = ''
    calls: str = ''
    operatorName: str = ''


def fetch_offers():
    urls = requests.get(app.constants.BASE_URL)
    raw_soup = BeautifulSoup(urls.text, features="html.parser")
    # <div class="offer-data">
    datas = raw_soup.find_all("div", {"class": "offer-data"})
    return [collect_data(data) for data in datas]


def collect_data(data) -> Offer:
    offer = Offer()
    offer.operatorName = "PLAY"
    offer.name = data.find("span", {"class": "sr-only"}).text
    offer.price = data.find("span", {"class": "price"}).text.replace("\n","")
    offer.loyaltyLenght = "24 miesiące"
    properties = data.find_all("li", {"class": "offer-property"})
    for prop in properties:
        arg = prop.find("p", {"class": "property-header"})
        field = arg.find("span", {"class": "property-name"}).text
        if "SMS" in field:
            offer.sms += f'{field} '
            offer.sms += prop.find("span", {"class": "tooltip-content"}).text.replace("\n", "")
        elif "rozmo" in field:
            offer.calls += f'{field} '
            offer.calls += prop.find("span", {"class": "tooltip-content"}).text.replace("\n", "")
        elif "internet" in field:
                offer.dataPacket += f'{field} '
                offer.dataPacket += prop.find("span", {"class": "tooltip-content"}).text.replace("\n", "")
        else:
                offer.priceFeatures += f'{field} '
                offer.priceFeatures += prop.find("span", {"class": "tooltip-content"}).text.replace("\n", "")
    if offer.calls is '':
        offer.calls = offer.sms
    return offer.__dict__

