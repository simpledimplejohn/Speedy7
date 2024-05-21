import requests
from django.conf import settings

class Rapid7API:
    base_url = "https://us.rest.logs.insight.rapid7.com"

    @staticmethod
    def get_headers():
        return {
            'x-api-key': settings.RAPID7_API_KEY,
            'Content-Type': 'application/json',
        }

    @classmethod
    def get_variables(cls):
        url = f"{cls.base_url}/query/variables"
        response = requests.get(url, headers=cls.get_headers())
        return response.json()
