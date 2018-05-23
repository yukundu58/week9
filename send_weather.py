# Prompts for a zip code
# and displays the current temperature
# and also sends it as a text message to your phone.

# Python 3.x
import keys
from sys import exit
from urllib.request import urlopen
from twilio.rest import Client
import json

zip = input("What's your zip code? ")

if len(zip) != 5:
    print("That's not a zip code!")
    exit(1)

if not zip.isdigit():
    print("That's not a zip code!")
    exit(1)

# Get current temperature from OpenWeatherMap.org

url = "http://api.openweathermap.org/data/2.5/weather?zip=" + zip + ",us&units=imperial&appid=" + keys.weather_api
raw_json = urlopen(url).read()
data = json.loads(raw_json)
temp = data['main']['temp']
print("It is", str(round(temp)), "degrees outside.")


# Send as text message


print()
print("(Press CTRL-C now if you do not want to send a text message)")
phone = input("What's your phone number (10 digits)? ")

if len(phone) != 10:
    print("That's not a phone number!")
    exit(1)

if not phone.isdigit():
    print("That's not a phone number!")
    exit(1)

phone_confirmation = input("Enter it again please (10 digits)? ")
if phone != phone_confirmation:
    print("Those phone numbers don't match.")
    exit(1)


client = Client(keys.account_sid, keys.auth_token)

sms_body = "It is " + str(round(temp)) + " degrees outside."
message = client.messages.create(
                              body= sms_body,
                              from_= keys.from_number,
                              to='+1' + phone
                          )

# If the message was successfully sent, the message object
# will have a "sid" property that you can access:
print("Message Sent! Tracking ID is:", message.sid)
