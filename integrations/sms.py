import requests

API_URL = ""

def send_sms(phone, text):
    payload = {
        "to": phone,
        "message": text
    }

    response = requests.postcls(API_URL, json=payload)
    return response.json()