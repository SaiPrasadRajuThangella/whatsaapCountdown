import os
from datetime import date, datetime
from twilio.rest import Client
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
from_whatsapp = os.getenv("TWILIO_WHATSAPP_NUMBER")
to_whatsapp = os.getenv("MY_WHATSAPP_NUMBER")
event_date = datetime.strptime(os.getenv("EVENT_DATE"), "%Y-%m-%d").date()

client = Client(account_sid, auth_token)

# Calculate countdown
today = date.today()
days_left = (event_date - today).days

# Send WhatsApp message
message = client.messages.create(
    from_=from_whatsapp,
    to=to_whatsapp,
    body=f"📅 Countdown: {days_left} days left until your event!"
)

print(f"Message sent! SID: {message.sid}")
