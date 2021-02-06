import sys
import requests
import json

ifttt_webhook_url = 'https://maker.ifttt.com/trigger/test_event/with/key/beREOf9nJV5yGL7aLFpS9b'
# requests.post(ifttt_webhook_url)

numbers = [1, 2, 3]

def numbers_increase():
    numbers = [n + 1 for n in numbers]
    return numbers

def get_crypto_data():
    with open('bitcoin_notifications/crypto_data.json') as f:
        return json.load(f)

data = get_crypto_data()

print(data["data"][0]["quote"]["USD"]["price"])