post_payload = {'factory': 'MOBILE', 'process': 'ACTIVATION', 'configComponentPk': '8796191445046',
                'suflerPk': '8796125854525', 'msisdn': ''}

headers = {'Connection': 'keep-alive',
           'Accept': 'application/json, text/plain',
           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36',
           'Content-Type': 'application/json;charset=UTF-8',
           'Origin': 'https://www.orange.pl',
           'Sec-Fetch-Site': 'same-origin',
           'Sec-Fetch-Mode': 'cors',
           'Sec-Fetch-Dest': 'empty',
           'Referer': 'https://www.orange.pl/abonament/abonament-komorkowy',
           'Accept-Language': 'pl-PL,pl;q=0.9,en-US;q=0.8,en;q=0.7'}

ORANGE_CSRF_URL = 'https://www.orange.pl/hapi/pwa/v1/offerSelector/getToken'
ORANGE_GETOFFERS_URL = 'https://www.orange.pl/hapi/pwa/v2/api/offers'


def getHeaders():
    return headers.copy()
