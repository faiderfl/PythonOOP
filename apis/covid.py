import requests
import pandas as pd

url= "https://api.covid19api.com/summary"
response= requests.get(url)
covid= response.json()

print(type(covid))

country_list=[]
for c in covid['Countries']:
    country_list.append([c['Country'], c['TotalConfirmed']])

covid_df= pd.DataFrame(country_list, columns=['Country', 'TotalConfirmed'])
print(covid_df.head())