
zodiacs = ["Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo", "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"]

userSign = input("What is your sign? ").capitalize()

while userSign not in zodiacs:
    print("That is not a valid zodiac sign")
    userSign = input("What is your sign? ").capitalize()

print(userSign)
