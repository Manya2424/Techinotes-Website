import requests
from django.core.mail.backends.base import BaseEmailBackend
from django.conf import settings

# API_TOKEN = 
# INBOX_ID = 

class MailtrapAPIBackend(BaseEmailBackend):
    def send_messages(self, email_messages):
        token = "b8a976836e1667330b26bb0ed7e58b0d"   # paste your token here
        inbox_id = "4691575"          # found in Mailtrap URL e.g. /inboxes/1234567

        sent = 0
        for msg in email_messages:
            payload = {
                "to": [{"email": r} for r in msg.to],
                "from": {"email": msg.from_email},
                "subject": msg.subject,
                "text": msg.body,
            }
            response = requests.post(
                f'https://sandbox.api.mailtrap.io/api/send/{inbox_id}',
                json=payload,
                headers={
                    "Authorization": f"Bearer {token}",
                    "Content-Type": "application/json"
                }
            )
            print("Payload:", payload)
            print("Status:", response.status_code)
            print("Response:", response.text)

            if response.status_code == 200:
                sent += 1
        return sent