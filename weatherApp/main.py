import requests
import json
import win32com.client as wincom
speak = wincom.Dispatch("SAPI.SpVoice")
city = input("Enter the name of the city\n")

url = f"https://api.weatherapi.com/v1/current.json?key=b13989793f184149a91141538230103&q={city}"

r = requests.get(url)
# print(r.text)
wdic = json.loads(r.text)
w = wdic["current"]["temp_c"]
print(w)
speak.Speak('the current weather in')
speak.Speak({city})
speak.Speak('is')
speak.Speak({w})
speak.Speak('degrees')