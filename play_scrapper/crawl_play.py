import app
from app import constants
import requests
import json

if __name__ == '__main__':
    json_off = app.fetch_offers()
    req = requests.post(constants.uri_offer, headers=constants.json_content_type,
                            data=json.dumps(json_off))
    print(req)
