from twilio.rest import Client

TWILIO_SID = "ACf3a87e59e8366b44a5248e4eaef45b35"
TWILIO_AUTH_TOKEN = "bc219af8ef0b4ed676b316070b2fa0ca"
TWILIO_VIRTUAL_NUMBER = "+13516668145"
TWILIO_VERIFIED_NUMBER = "+420733500891"


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)
