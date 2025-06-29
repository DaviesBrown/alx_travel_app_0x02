import requests
from django.conf import settings

class PaystackClient:
    base_url = settings.PAYSTACK_BASE_URL
    headers  = {
        "Authorization": f"Bearer {settings.PAYSTACK_SECRET_KEY}",
        "Content-Type": "application/json",
    }

    @classmethod
    def initialize(cls, email, amount, callback_url):
        url     = f"{cls.base_url}/transaction/initialize"
        payload = {
            "email": email,
            "amount": amount,       # in kobo
            "callback_url": callback_url,
        }
        return requests.post(url, json=payload, headers=cls.headers).json()

    @classmethod
    def verify(cls, reference):
        url = f"{cls.base_url}/transaction/verify/{reference}"
        return requests.get(url, headers=cls.headers).json()
