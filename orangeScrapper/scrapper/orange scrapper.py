from pprint import pprint

import requests
import json
import constants
import re

class Offer:
    name: str = ''
    price: float = ''
    loyaltyLenght: int = ''
    featureList:str = ''
    priceFeatures: str = ''
    def __str__(self):
        return f"name: {self.name}, \n" \
               f"price: {self.price}, \n" \
               f"loyaltyLenght: {self.loyaltyLenght}, \n" \
               f"featureList: {self.featureList}, \n" \
               f"priceFeatures: {self.priceFeatures}"

token = requests.get(constants.ORANGE_CSRF_URL)
csrftoken = token.text.replace('\"', "")
# update headers with csrfheader
post_headers = constants.getHeaders()
post_headers.update({'csrftoken': csrftoken})

offers = requests.post(constants.ORANGE_GETOFFERS_URL, cookies=token.cookies, headers=post_headers,
                       data=json.dumps(constants.post_payload))

offers_collection = list

#Regex to clean up junk htmls leftovers
clean = re.compile('<.*?>')

#TODO split every iteration and scrapping of json properpties to separate function for clarification
for iter in offers.json():
    offer = Offer()
    offer.loyaltyLenght = f"{iter['loyaltyLength']} miesiące"
    offer.price = (iter['tieredPriceList'][0].get('basePrice'))
    for arg in iter['mainServices']:
        #cleaner = Cleaner(allow_tags=[''], remove_unknown_tags=False)
        features = arg['features']
        offer.name = features\
            .get('config')[0]\
            .get('value')\
            .get('Name')
        priceDescription = features.get('priceFeatures')[0].get('value').get('priceDescription')
        boxFeatures = features.get('boxFeatures')
        for var in boxFeatures[0].get('value').get('value'):
            offer.featureList += f"{var.get('name')}\n"
            if var.get('description') is not None:
                offer.featureList += f"{var.get('description')}\n"
            offer.featureList += f"{var.get('value')} \n"
        offer.priceFeatures =re.sub(clean, '', priceDescription)
    print(offer)
    print("_______________________________________________________________________________")
