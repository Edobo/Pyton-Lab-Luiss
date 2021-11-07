import requests

cities = ['Vienna', 'Brussels', 'Moscow']
latitude = ['48.2092', '50.8371', '55.7558']
longitude = ['16.3728', '4.3676', '37.6176']

for i in range (0,3):
    url = 'https://api.open-meteo.com/v1/forecast?latitude='+latitude[i]+'&longitude='+longitude[i]+'&hourly=temperature_2m,pressure_msl,precipitation,snow_height'
    response = requests.get(url)
    file = open("./file-data_"+cities[i]+".json", "w+")
    print(file.name)
    file.writelines(response.text)
    file.close()

import json
import pandas
time = []
temperature = []
pressure = []
precipitation = []
snow_height = []
l = []
for j in range(0,3):
    dati_json = json.load(open("./file-data_"+cities[j]+".json"))
    for h in dati_json["hourly"]["time"]:
        time.append(h)
    for h in dati_json["hourly"]["temperature_2m"]:
        temperature.append(h)
    for h in dati_json["hourly"]["pressure_msl"]:
        pressure.append(h)
    for h in dati_json["hourly"]["precipitation"]:
        precipitation.append(h)
    for h in dati_json["hourly"]["snow_height"]:
        snow_height.append(h)
    for k in range(0,len(temperature)):
        n = [cities[j], time[k], temperature[k], pressure[k], precipitation[k], snow_height[k]]
        l.append(n)

csv_file_path = 'meteo.csv'
df = pandas.DataFrame(l)
df.columns = ['city', 'time', 'temperature', 'pressure', 'precipitation', 'snow_height']
df.to_csv(csv_file_path, index = False)

