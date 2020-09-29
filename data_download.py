import urllib.parse, requests
from bs4 import BeautifulSoup
r = requests.get("http://www.bitcoinexchangerate.org/") # get response from bitcoinexchange

newhtml = BeautifulSoup(r.text,"html.parser") # parse into html using BeautifulSoup


titleString = newhtml.title.string
priceString = ""

for c in titleString:
    if c.isdigit() or c == ".":
        priceString = priceString + c
    else:
         if c == "U":
             break

print(priceString)

history_url = 'https://production.api.coindesk.com/v2/price/values/BTC'
data = {}
data['start_date'] = '2020-08-27T08:00'

data['end_date'] = '2020-09-27T08:00'
data['ohlc'] = 'true'
parsedData = urllib.parse.urlencode(data)


response_2 = requests.get(history_url, parsedData)

json_data = response_2.json()["data"]["entries"]

import numpy as np
numpy_data = np.array(json_data)
