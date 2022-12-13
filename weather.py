import requests
import json

import requests

location = input("Enter State/Country  ")
url = "https://visual-crossing-weather.p.rapidapi.com/forecast"

querystring = {"aggregateHours":"24","location":location,"contentType":"json"}

headers = {
	"X-RapidAPI-Key": "d20a16e73dmsh40a1ef627fe69ebp187596jsn45f113b23412",
	"X-RapidAPI-Host": "visual-crossing-weather.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

a = response.json()

u = a['locations']


for i in u:
    if u[i]['currentConditions'] == {}:
        print("No Weather Record")
    else:
        print("Sunrise - ",u[i]['currentConditions']['sunrise'])
        print("moonphase - ",u[i]['currentConditions']['moonphase'])
        print("cloudcover - ",u[i]['currentConditions']['cloudcover'])
        print("sealevelpressure - ",u[i]['currentConditions']['sealevelpressure'])
        print("dew - ",u[i]['currentConditions']['dew'])
        print("sunset - ",u[i]['currentConditions']['sunset'])
        print("windchill - ",u[i]['currentConditions']['windchill'])
        print("Temperature - ",u[i]['currentConditions']['temp'])
        print("Wind Speed - ",u[i]['currentConditions']['wspd'])
    