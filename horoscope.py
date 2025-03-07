import requests
import json

def getHoroscope():

    zodiacs = ["Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo", "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"]
    userSign = input("What is your sign? ").capitalize()

    while userSign not in zodiacs:
        print("That is not a valid zodiac sign")
        userSign = input("What is your sign? ").capitalize()

    url = "https://horoscope-app-api.vercel.app/api/v1/get-horoscope/daily"
    params = {
        "sign": userSign,
        "day": "TODAY"
    }

    headers = {
        "accept": "application/json"
    }

    response = requests.get(url, params=params, headers=headers)

    if response.status_code == 200:
        data = response.json()
        horoscope_data = data["data"]["horoscope_data"]
    else:
        print(f"Error: {response.status_code}")
    
    return horoscope_data



