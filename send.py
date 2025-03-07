import os
import horoscope
from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv()
TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")

account_sid = TWILIO_ACCOUNT_SID
auth_token = TWILIO_AUTH_TOKEN

client = Client(account_sid, auth_token)

from_whatsapp_number = "whatsapp:+14155238886"
to_whatsapp_number = "whatsapp:+4791166190"

client.messages.create(body=horoscope.getHoroscope(),
                       from_=from_whatsapp_number,
                       to=to_whatsapp_number)