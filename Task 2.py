import requests

cities = ['Vienna', 'Brussels', 'Moscow', 'Paris', 'Reykjavik', 'New York', 'Ottawa']
latitude = ['48.2092', '50.8371', '55.7558', '48.8567', '64.1353', '40.71', '45.4235']
longitude = ['16.3728', '4.3676', '37.6176', '2.3510', '-21.8952', '-74.01', '-75.6979']
for i in range (0,len(cities)):
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
for j in range(0,len(cities)):
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
    time = []
    temperature = []
    pressure = []
    precipitation = []
    snow_height = []

csv_file_path = 'meteo.csv'
df = pandas.DataFrame(l)
df.columns = ['city', 'time', 'temperature', 'pressure', 'precipitation', 'snow_height']
df.to_csv(csv_file_path, index = False)

import pandas as pd
import matplotlib.pyplot as plt
df.head()
df.shape

df['time'] = pd.to_datetime(df['time'])
i=0
plt.figure (figsize=(10,5))
c = ["red", "blue", "green", "yellow", "purple", "orange", "black"]
for city in cities:
    df_V = df[df['city']==city]
    plt.plot(df_V['time'],df_V['temperature'],marker='.', color=c[i])
    i=i+1

plt.legend(cities)
plt.xlabel("Time")
plt.ylabel("Temperature 2m")
plt.title("Air temperature at 2 meters above ground")
plt.show()

df['time'] = pd.to_datetime(df['time'])
i=0
plt.figure (figsize=(10,5))
c = ["red", "blue", "green", "yellow", "purple", "orange", "black"]
for city in cities:
    df_V = df[df['city']==city]
    plt.plot(df_V['time'],df_V['pressure'],marker='.', color=c[i])
    i=i+1

plt.legend(cities)
plt.xlabel("Time")
plt.ylabel("pressure_msl")
plt.title("Atmospheric air pressure reduced to sea level")
plt.show()

df['time'] = pd.to_datetime(df['time'])
i=0
plt.figure (figsize=(10,5))
c = ["red", "blue", "green", "yellow", "purple", "orange", "black"]
for city in cities:
    df_V = df[df['city']==city]
    plt.plot(df_V['time'],df_V['precipitation'],marker='.', color=c[i])
    i=i+1

plt.legend(cities)
plt.xlabel("Time")
plt.ylabel("precipitation")
plt.title("Total precipitation (rain, showers, snow) sum of the preceding hour")
plt.show()

df['time'] = pd.to_datetime(df['time'])
i=0
plt.figure (figsize=(10,5))
c = ["red", "blue", "green", "yellow", "purple", "orange", "black"]
for city in cities:
    df_V = df[df['city']==city]
    plt.plot(df_V['time'],df_V['snow_height'],marker='.', color=c[i])
    i=i+1

plt.legend(cities)
plt.xlabel("Time")
plt.ylabel("Snow Height")
plt.title("Snow height from the ground")
plt.show()