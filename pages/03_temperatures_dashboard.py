import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st


data_path = "data/cities_temperatures.csv"

temps_df = pd.read_csv(data_path)

temps_df["Date"] = pd.to_datetime(temps_df["Date"]).dt.date

temps_df["AvgTemperatureCelsius"] = ((temps_df['AvgTemperatureFahrenheit'] - 32)/1.8).round(1)

temps_df

city_list = temps_df['City'].unique().tolist()

unique_countries_list = len(city_list)

f'There are {unique_countries_list} unique cities in this dataset'

min_date = temps_df['Date'].min()
max_date = temps_df['Date'].max()

f'Min date is {min_date}, Max date is {max_date}'

min_temp = temps_df['AvgTemperatureCelsius'].min()
max_temp = temps_df['AvgTemperatureCelsius'].max()

min_temp_city = temps_df.loc[temps_df['AvgTemperatureCelsius'] == temps_df['AvgTemperatureCelsius'].min(),:]['City'].iloc[0]
min_temp_date = temps_df.loc[temps_df['AvgTemperatureCelsius'] == temps_df['AvgTemperatureCelsius'].min(),:]['Date'].iloc[0]

max_temp_city = temps_df.loc[temps_df['AvgTemperatureCelsius'] == temps_df['AvgTemperatureCelsius'].max(),:]['City'].iloc[0]
max_temp_date = temps_df.loc[temps_df['AvgTemperatureCelsius'] == temps_df['AvgTemperatureCelsius'].max(),:]['Date'].iloc[0]

f'Min temp was {min_temp} in {min_temp_city} on {min_temp_date}. Max temp was {max_temp} in {max_temp_city} on {max_temp_date}'

city = "Munich"
start_date = pd.to_datetime("2008-01-01").date()
end_date = pd.to_datetime("2010-12-31").date()

city_df = temps_df[temps_df['City'] == city]

city_df_period = city_df[(city_df['Date'] >= start_date) & (city_df['Date'] <= end_date)]

fig = plt.figure(figsize=(10, 5))

plt.plot(city_df_period['Date'], city_df_period['AvgTemperatureCelsius'])
plt.title(f'Plot Munich between {start_date} and {end_date}')
plt.xlabel('Date')
plt.ylabel('AvgTemperatureCelsius')
plt.legend(['Munich'])

plt.show()

st.pyplot(fig)

fig = plt.figure(figsize=(10, 5))

plt.hist(city_df_period['AvgTemperatureCelsius'])
plt.title(f'Histplot Munich between {start_date} and {end_date}')
plt.xlabel('Value')
plt.ylabel('AvgTemperatureCelsius')
plt.legend(['Munich'])

st.pyplot(fig)
selected_cities = ["Munich", "Buenos Aires", "Tokyo"]
start_date = pd.to_datetime("2008-01-01").date()
end_date = pd.to_datetime("2010-12-31").date()

cities_df = temps_df[temps_df['City'].isin(selected_cities)]

cities_df_period = cities_df[(cities_df['Date'] >= start_date) & (cities_df['Date'] <= end_date)]

fig = plt.figure(figsize=(15, 5))

for city in selected_cities:
    plt.plot(cities_df_period[cities_df_period['City'] == city]['Date'], cities_df_period[cities_df_period['City'] == city]['AvgTemperatureCelsius'])

plt.title(f'Temperature between {start_date} and {end_date} in {', '.join(selected_cities)}')
plt.xlabel('Date')
plt.ylabel('AvgTemperatureCelsius')

plt.legend(selected_cities)

st.pyplot(fig)

selected_cities = ["Munich", "Buenos Aires", "Tokyo"]
start_date = pd.to_datetime("2008-01-01").date()
end_date = pd.to_datetime("2010-12-31").date()

cities_df = temps_df[temps_df['City'].isin(selected_cities)]

cities_df_period = cities_df[(cities_df['Date'] >= start_date) & (cities_df['Date'] <= end_date)]

fig = plt.figure(figsize=(15, 5))

for city in selected_cities:
    plt.hist(cities_df_period[cities_df_period['City'] == city]['AvgTemperatureCelsius'])
    
plt.title(f'Histplot {', '.join(selected_cities)} between {start_date} and {end_date}')
plt.xlabel('Value')
plt.ylabel('AvgTemperatureCelsius')

plt.legend(selected_cities)

st.pyplot(fig)
