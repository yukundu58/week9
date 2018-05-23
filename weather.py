# This is the weather module.
# This is the weather module.

import keys
from sys import exit
from urllib.request import urlopen
from twilio.rest import Client
import json

def send_weather(zip, phone):

    if len(str(zip)) != 5:
        print("That's not a zip code!")
        return

    if type(zip) != int:
        print("That's not a zip code!")
        return

    if len(str(phone)) != 10:
        print("That's not a phone number!")
        return

    if type(phone) != int:
        print("That's not a phone number!")
        return

    url = "http://api.openweathermap.org/data/2.5/weather?zip=" + str(zip) + ",us&units=imperial&appid=" + keys.weather_api
    raw_json = urlopen(url).read()
    data = json.loads(raw_json)
    temp = data['main']['temp']

    client = Client(keys.account_sid, keys.auth_token)

    sms_body = "It is " + str(round(temp)) + " degrees outside."
    message = client.messages.create(
                              body= sms_body,
                              from_= keys.from_number,
                              to='+1' + str(phone)
                          )

    print("It is", str(round(temp)), "degrees outside.")
    print("Message Sent! Tracking ID is:", message.sid)
    return


if __name__ == '__main__':
    send_weather(60615, 2179790839)
