import requests
import json
import time
import matplotlib.pyplot as plt
import datetime
import keys

start_time = time.time()


def getData():
    url = "https://daily-atmosphere-carbon-dioxide-concentration.p.rapidapi.com/api/co2-api"
    KEY = keys.KEY
    headers = {
        "X-RapidAPI-Key": f"{KEY}",
        "X-RapidAPI-Host": "daily-atmosphere-carbon-dioxide-concentration.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers).json()
    with open("jsonDoc.json", "w") as outfile:
        json.dump(response, outfile, indent=4)


file = open("jsonDoc.json")
data = json.load(file)
file.close()


def toDate(year, month, day):
    return datetime.datetime(int(year), int(month), int(day))

x = []
y = []
print(len(data['co2']))
for day in data['co2']:
    date = toDate(day['year'],day['month'],day['day'])
    x.append(date)
    y.append(float(day['cycle']))

plt.plot(x, y)
plt.xlabel('Date')
plt.ylabel('CO2 in Atmosphere')
print ("My program took", time.time() - start_time, "to run")
plt.show()