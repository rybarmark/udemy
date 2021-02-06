#Note! For the code to work you need to replace all the placeholders with
#Your own details. e.g. account_sid, lat/lon, from/to phone numbers.

import requests
import os
import venv
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
# openweather_api_key = "b108a9dd0b30d1df2ec17604c3289d11"
# api_key = venv.get("OWM_API_KEY")
# print(os.environ)

api_key = os.environ.get("OWM_API_KEY")

account_sid = "ACf3a87e59e8366b44a5248e4eaef45b35"
auth_token = "bc219af8ef0b4ed676b316070b2fa0ca"

weather_params = {
    "lat": "50.142448",
    "lon": "15.116640",
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    proxy_client = TwilioHttpClient()
    # proxy_client.session.proxies = {'https': os.environ['https_proxy']} 
    # proxy_client.session.proxies = {'https': 'http://proxy.server:3128'}

    client = Client(account_sid, auth_token, http_client=proxy_client)
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an ☔️",
        from_="+13516668145",
        to="+420733500891"
    )
    print(message.status)
