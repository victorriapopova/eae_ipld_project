import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

# Ex 3.1: Load the dataset from the defined data_path and display the first 5 rows.

data_path = "data/cities_temperatures.csv"

# Load the dataset into a pandas DataFrame
temps_df = pd.read_csv(data_path)

# Display the first 5 rows of the dataframe
temps_df

# Converting the date column to datetime date format in order to be able to analyze better the time series and plot it
temps_df["Date"] = pd.to_datetime(temps_df["Date"]).dt.date

# Assuming AvgTemperature is in Fahrenheit, we convert it to Celsius
temps_df['AvgTemperatureCelsius'] = (temps_df['AvgTemperature'] - 32) * 5 / 9

# Display the first few rows to verify the new column
temps_df[['AvgTemperature', 'AvgTemperatureCelsius']].head()

# Ex 3.2: Create a new column called `AvgTemperatureCelsius` that contains the temperature in Celsius degrees.

# temps_df["AvgTemperatureCelsius"] = ...  # TODO: uncomment this line to complete it

# Ex 3.2: Create a new column called `AvgTemperatureCelsius` that contains the temperature in Celsius degrees.
# Ensure that you are working with the correct column for temperature in Fahrenheit
# In your case, it seems to be 'AvgTemperatureFahrenheit'
temps_df["AvgTemperatureCelsius"] = (temps_df["AvgTemperatureFahrenheit"] - 32) * 5 / 9

# Display the first few rows to check if the new column has been added
temps_df.head()

# Ex 3.3: How many different cities are there? Provide a list of them.

 # TODO: this should be a list of unique countries

# TODO: print a message with the number of unique countries and the list of them
# Ex 3.3: How many different cities are there? Provide a list of them.

# Get the list of unique cities
unique_cities_list = temps_df['City'].unique()

# Get the number of unique cities
num_unique_cities = len(unique_cities_list)

# Print the result
f"There are {num_unique_cities} different cities in the dataset."
f"List of unique cities: {unique_cities_list}"

# Ex 3.4: What are the minimum and maximum dates?

# Ex 3.4: What are the minimum and maximum dates?

# Get the minimum and maximum dates
min_date = temps_df['Date'].min()
max_date = temps_df['Date'].max()

# Print the result
f"The minimum date is {min_date}"
f"The maximum date is {max_date}"


# Ex 3.5: What are the global minimum and maximum temperatures? Find the city and the date of each of them.
# Finding the minimum temperature
# Make sure the 'AvgTemperatureCelsius' column is created

# Now proceed with the task for minimum and maximum temperatures
# Check if 'AvgTemperatureCelsius' exists in the DataFrame
# Check if 'AvgTemperatureCelsius' exists in the DataFrame
print(temps_df.columns)  # This will list all columns to confirm if 'AvgTemperatureCelsius' exists.

# Finding the minimum temperature
min_temp = temps_df["AvgTemperatureCelsius"].min()
min_temp_row = temps_df[temps_df["AvgTemperatureCelsius"] == min_temp].iloc[0]
min_temp_city = min_temp_row["City"]

# Extract year, month, and day from the Date column
min_temp_date = min_temp_row["Date"].strftime('%Y-%m-%d')  # Ensure the Date column is a datetime object

# Finding the maximum temperature
max_temp = temps_df["AvgTemperatureCelsius"].max()
max_temp_row = temps_df[temps_df["AvgTemperatureCelsius"] == max_temp].iloc[0]
max_temp_city = max_temp_row["City"]

# Extract year, month, and day from the Date column
max_temp_date = max_temp_row["Date"].strftime('%Y-%m-%d')  # Ensure the Date column is a datetime object

# Print the results
f"The global minimum temperature is {min_temp:.2f}°C in {min_temp_city} on {min_temp_date}."
f"The global maximum temperature is {max_temp:.2f}°C in {max_temp_city} on {max_temp_date}."



# Ex 3.6: For a given city and a range of dates (start and end):
#   - Make a line plot with the temperature reads of that city during the selected time period, the x axis has to be the timestamp column.
#   - Make a histogram of the temperature reads of that city during the selected time period.
#   - Make sure that all plots include a title, axis labels and a legend.


# Given city and date range
city = "Munich"
start_date = pd.to_datetime("2008-01-01").date()
end_date = pd.to_datetime("2010-12-31").date()

# Step 1: Filter the DataFrame for the selected city
city_df = temps_df[temps_df["City"] == city]

# Step 2: Filter the DataFrame for the selected time period
city_df_period = city_df[(city_df["Date"] >= start_date) & (city_df["Date"] <= end_date)]

# Step 3: Line Plot of AvgTemperatureCelsius over time
fig = plt.figure(figsize=(10, 5))
plt.plot(city_df_period["Date"], city_df_period["AvgTemperatureCelsius"], label="AvgTemperatureCelsius", color='blue')
plt.title(f"Temperature in {city} from {start_date} to {end_date}")
plt.xlabel("Date")
plt.ylabel("Temperature (°C)")
plt.legend()

# Show the line plot
st.pyplot(fig)

# Step 4: Histogram of temperature readings
fig1 = plt.figure(figsize=(10, 5))
plt.hist(city_df_period["AvgTemperatureCelsius"], bins=20, color='green', edgecolor='black', alpha=0.7)
plt.title(f"Temperature Distribution in {city} from {start_date} to {end_date}")
plt.xlabel("Temperature (°C)")
plt.ylabel("Frequency")
plt.legend(["Temperature Distribution"])

# Show the histogram
st.pyplot(fig1)

# TODO: Build the histogram plot using the city_df_period AvgTemperatureCelsius column as the data to plot

# Plotting the histogram for AvgTemperatureCelsius
fig2 = plt.figure(figsize=(10, 5))

# Step 1: Create the histogram using the AvgTemperatureCelsius column
plt.hist(city_df_period["AvgTemperatureCelsius"], bins=20, color='green', edgecolor='black', alpha=0.7)

# Step 2: Add title and labels
plt.title(f"Temperature Distribution in {city} from {start_date} to {end_date}")
plt.xlabel("Temperature (°C)")
plt.ylabel("Frequency")

# Step 3: Show the plot
st.pyplot(fig2)


# Ex 3.7: Now repeat the previous question but for a list of cities:
#   - Make a line plot with the temperature reads of the cities in the list, for the selected time period, every city has to be a different line with a different color, the x axis has to be the timestamp column.
#   - Make a histogram of the temperature reads of a list of selected cities, for the selected time period, every city has to be its own distribution with a different color.
#   - Make sure that all plots include a title, axis labels and a legend.
import matplotlib.pyplot as plt

# Step 1: Prepare the list of cities, date range, and plot figure
selected_cities = ["Munich", "Buenos Aires", "Tokyo"]
start_date = pd.to_datetime("2008-01-01").date()
end_date = pd.to_datetime("2010-12-31").date()

plt.figure(figsize=(15, 5))

# Step 2: Loop over each city and plot the line chart for AvgTemperatureCelsius over time
for city in selected_cities:
    # Get the data for the selected city and within the specified date range
    city_df = temps_df[temps_df["City"] == city]  # Get the rows for the city
    city_df_period = city_df[(city_df["Date"] >= start_date) & (city_df["Date"] <= end_date)]  # Filter by date range

    # Plot the line chart for the city's temperature
    plt.plot(city_df_period["Date"], city_df_period["AvgTemperatureCelsius"], label=city)

# Step 3: Add title and labels to the plot
plt.title(f"Temperature over Time for Selected Cities ({start_date} to {end_date})")
plt.xlabel("Date")
plt.ylabel("Temperature (°C)")

# Step 4: Show the legend
plt.legend()

# Step 5: Display the plot
plt.show()

# Step 6: Create a histogram for the selected cities' temperature distributions
fig3 = plt.figure(figsize=(15, 5))

# Step 7: Loop over each city again to plot the histogram
for city in selected_cities:
    # Get the data for the selected city and within the specified date range
    city_df = temps_df[temps_df["City"] == city]  # Get the rows for the city
    city_df_period = city_df[(city_df["Date"] >= start_date) & (city_df["Date"] <= end_date)]  # Filter by date range

    # Plot the histogram for the city's temperature distribution
    plt.hist(city_df_period["AvgTemperatureCelsius"], bins=20, alpha=0.7, label=city)

# Step 8: Add title and labels to the histogram
plt.title(f"Temperature Distribution for Selected Cities ({start_date} to {end_date})")
plt.xlabel("Temperature (°C)")
plt.ylabel("Frequency")

# Step 9: Show the legend
plt.legend()

# Step 10: Display the histogram
st.pyplot(fig3)


# TODO: Build the histogram plot for the selected cities using the city_df_period AvgTemperatureCelsius column as the data to plot for each one

# Selected cities and the date range for plotting
selected_cities = ["Munich", "Buenos Aires", "Tokyo"]
start_date = pd.to_datetime("2008-01-01").date()
end_date = pd.to_datetime("2010-12-31").date()

# Create a figure for the histogram
fig4 = plt.figure(figsize=(15, 5))

# Loop through each city in the selected cities list
for city in selected_cities:
    # Filter the dataframe for the current city
    city_df = temps_df[temps_df["City"] == city]

    # Filter the dataframe further for the selected time period
    city_df_period = city_df[(city_df["Date"] >= start_date) & (city_df["Date"] <= end_date)]

    # Plot the histogram for the city's temperature in Celsius
    plt.hist(city_df_period["AvgTemperatureCelsius"], bins=20, alpha=0.7, label=city)

# Add title and axis labels
plt.title(f"Temperature Distribution for Selected Cities ({start_date} to {end_date})")
plt.xlabel("Temperature (°C)")
plt.ylabel("Frequency")

# Show the legend
plt.legend()

# Display the histogram plot
st.pyplot(fig4)

