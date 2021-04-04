# Download the helper library from https://www.twilio.com/docs/python/install
import os
import datetime
from twilio.rest import Client
import time
import atexit

from apscheduler.schedulers.background import BackgroundScheduler

account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

# Make this into a flask app that runs every 24 hours https://stackoverflow.com/questions/21214270/how-to-schedule-a-function-to-run-every-hour-on-flask

# figure. outthe time using date Time
# when it's a certain time, send the message?
current = datetime.datetime.now()
print(current.strftime("%H:%M.%s"))


def print_date_time():
  # message = client.messages \
  #   .create(
  #     body="Don't forget to make tea",
  #     from_='+15202146801',
  #     to=os.environ['TEST_PHONE_NUMBER']
  #   )
  print("triggered")
  print(time.strftime("%A, %d. %B %Y %I:%M:%S %p"))

scheduler = BackgroundScheduler()
scheduler.add_job(func=print_date_time, trigger="interval", seconds=10)
scheduler.start()

# Shut down the scheduler when exiting the app
atexit.register(lambda: scheduler.shutdown())

# print(message.sid)
