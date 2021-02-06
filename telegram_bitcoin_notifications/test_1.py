import sys
import requests
from requests import Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import test_2

ifttt_key = 'beREOf9nJV5yGL7aLFpS9b'

blockchain_url = 'https://blockchain.info/ticker'
bitcoin_api = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
ifttt_webhooks_url = 'https://maker.ifttt.com/trigger/{}/with/key/' + ifttt_key

parameters = {
  'start':'1',
  'limit':'5000',
  'convert':'USD'
}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': '4f6e3841-e38d-4c52-b942-d7e376912536',
}

session = Session()
session.headers.update(headers)

data = ''

try:
  response = session.get(bitcoin_api, params=parameters)
  data = json.loads(response.text)
  print(data)
except (ConnectionError, Timeout, TooManyRedirects) as e:
  print(e)

def get_latest_bitcoin_price():
  return float(data["data"][0]["quote"]["USD"]["price"])

bitcoin_price = get_latest_bitcoin_price()

def post_ifttt_webhook(event, value):
  data = {'value1': value}
  ifttt_event_url = ifttt_webhooks_url.format(event)
  requests.post(ifttt_event_url, json=data)

try:
  post_ifttt_webhook('bitcoin_price_update', bitcoin_price)
  print(bitcoin_price)
except (ConnectionError, Timeout, TooManyRedirects) as e:
  print(e)