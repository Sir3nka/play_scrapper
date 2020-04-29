import request
import json
from bs4 import BeautifulSoup

#Helios scrapper, let's try to make it as generic as possible to maybe load configuration

REPERTUAR_URL = "https://www.helios.pl/47,Lodz/Repertuar/"




def fetch_repertuar_urls():
    raw_html = request.get(REPERTUAR_URL)
    return

def collect_repertuars_urls(arg)