# import urllib.parse, requests
# from bs4 import BeautifulSoup
# r = requests.get("http://www.bitcoinexchangerate.org/") # get response from bitcoinexchange
#
# newhtml = BeautifulSoup(r.text,"html.parser") # parse into html using BeautifulSoup
#
#
# titleString = newhtml.title.string
# priceString = ""
#
# for c in titleString:
#     if c.isdigit() or c == ".":
#         priceString = priceString + c
#     else:
#          if c == "U":
#              break
#
# print(priceString)
#
# history_url = 'https://production.api.coindesk.com/v2/price/values/BTC'
# data = {}
# data['start_date'] = '2020-08-27T08:00'
#
# data['end_date'] = '2020-09-27T08:00'
# data['ohlc'] = 'true'
# parsedData = urllib.parse.urlencode(data)
#
#
# response_2 = requests.get(history_url, parsedData)
#
# json_data = response_2.json()["data"]["entries"]
#
# import numpy as np
# numpy_data = np.array(jsondata)
from datetime import datetime
from urllib.parse import urlencode
import requests
import numpy as np
from bs4 import BeautifulSoup


class BitcoinScraper:

    def __init__(self, hurl= "https://production.api.coindesk.com/v2/price/values/BTC", rurl = 'http://www.bitcoinexchangerate.org/'):
        self.hurl = hurl
        self.rurl = rurl

    def getHistoricalData(self, start_time, end_time, ohlc):
        values = {}
        values['start_date'] = start_time
        values['end_date'] = end_time
        values['ohlc'] = ohlc
        urldata = urlencode(values)
        response = requests.get(self.hurl, urldata)
        jsonResp = response.json()
        data = jsonResp['data']['entries']
        data = np.array(data)
        return data

    def getRealTimeData(self, printPrice=True):
        rawhtml = requests.get(self.rurl).text
        site = BeautifulSoup(rawhtml, features='html.parser')
        titleString = site.title.string
        priceString = ""

        for char in titleString:
            if char.isdigit() or char == ".":
                priceString += char  # add digit to string
            elif (char == 'U'):  # end on the USD
                priceString = priceString.strip()
                break
        if printPrice == True:
            print('Real time Bitcoin price is:\n$' + priceString)
        return priceString
