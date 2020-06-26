#!/usr/bin/python

import pandas as pd
import json
import requests
import os

cwd = os.getcwd()

city = raw_input('Enter the city: ')
country = raw_input('Enter the country: ')

# city = 'Krakow'
#country = 'Poland'
#date_ = "2020-02-11"

# retrieve json file
# url = "https://api.midway.tomtom.com/ranking/live/ITA_milan"
# url = "https://api.weather.midway.tomtom.com/weather/live/ITA_milan"
# url = "https://api.midway.tomtom.com/ranking/dailyStats/ITA_milan"

url = "https://api.midway.tomtom.com/ranking/dailyStats/"+country[0:3].upper()+"_"+city.lower()
#url = "https://api.midway.tomtom.com/ranking/dailyStats/CHN_"+city.lower()
req_ = requests.get(url)
json_ = req_.json()

pd.set_option("display.max_rows", False)

df = pd.DataFrame.from_dict(json_)
df['date'] = pd.DataFrame(df['date'], columns=['date'])
df['datetime'] = pd.to_datetime(df['date'])
df = df.set_index('datetime')
df.drop(['date'], axis=1, inplace=True)

#df.head()
df['week'] = df['week'].astype(str).str[:-5]

# plt.style.use("ggplot")
# ax = df.plot(color="Green")
# plt.title(city + " Traffic")
# plt.legend(loc=2)
# plt.box(False)

#df.loc[df.index.strftime("%Y-%m-%d") == date_]


df.to_csv(cwd+"/"+city.lower()+'_traffic.csv', encoding = 'utf-8')

print("Succeessful. Check out "+cwd+"/"+city.lower()+'_traffic.csv file.')
