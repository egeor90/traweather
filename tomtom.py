#!/usr/bin/python

import pandas as pd
import json
import requests
import os

city = 'Moscow'
country = 'Russia'
#date_ = "2020-02-11"

# retrieve json file
url = "https://api.midway.tomtom.com/ranking/dailyStats/"+country[0:3].upper()+"_"+city.lower()
#url = "https://api.midway.tomtom.com/ranking/dailyStats/CHN_"+city.lower()

req_ = requests.get(url)
json_ = req_.json()

pd.set_option("display.max_rows", False)

# Convert to pandas DataFrame
df = pd.DataFrame.from_dict(json_)
df['date'] = pd.DataFrame(df['date'], columns=['date'])
df['datetime'] = pd.to_datetime(df['date'])
df = df.set_index('datetime')
df.drop(['date'], axis=1, inplace=True)

df['week'] = df['week'].astype(str).str[:-5]

df.to_csv(os.getcwd()+"/"+city.lower()+'_traffic.csv', encoding = 'utf-8')
