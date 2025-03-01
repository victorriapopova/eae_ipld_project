import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

# Ex 2.1: Load the data using Pandas read_csv, use `show_id` as the index_col parameter.

data_path = "data/netflix_titles.csv"

# Load the data into a Pandas DataFrame, using 'show_id' as the index column
movies_df = pd.read_csv(data_path, index_col="show_id")

# Display the DataFrame
movies_df

# Ex 2.2: What is the min and max release years?

# Ex 2.2: Find the minimum and maximum release years
min_year = movies_df["release_year"].min()  # Find the minimum release year
max_year = movies_df["release_year"].max()  # Find the maximum release year

# Print the results
f"Min year: {min_year}, Max year: {max_year}"

# Ex 2.3: Count the number of missing values (NaN) in the 'director' column
num_missing_directors = movies_df["director"].isna().sum()

# Print the result
f"Number of missing directors: {num_missing_directors}"
year = 2005

# Step 3: Filter data by the given year
filtered_df = movies_df[movies_df['release_year'] == year]

# Step 4: Handle rows where 'country' column contains multiple countries
# Split the countries by comma, strip spaces, and flatten the list
countries_list = filtered_df['country'].dropna().apply(lambda x: [country.strip() for country in x.split(',')]).explode()

# Step 5: Get the number of movies/series for each country
top_10_countries = countries_list.value_counts().head(10)

# Step 6: Print the result
f"Top 10 countries: {top_10_countries}"

# Step 7: Plot the pie chart
fig = plt.figure(figsize=(8, 8))
plt.pie(top_10_countries, labels=top_10_countries.index, autopct="%.2f%%")
plt.title(f"Top 10 Countries in {year}")
st.pyplot(fig)


# Step 1: Fill missing values in the 'country' column with "Unknown"
movies_df["country"] = movies_df["country"].fillna("Unknown")

# Step 2: Handle multiple countries in a list and join them into a single string
# First, we need to ensure the countries are in list format and then join them into a single string.
# If the country column contains lists, we join the elements; otherwise, we keep the value as is.

def process_countries(countries):
    if isinstance(countries, str):
        # If it's a string, just return it
        return countries
    elif isinstance(countries, list):
        # If it's a list, join the elements with ", "
        return ", ".join(countries)
    else:
        return "Unknown"

# Apply the function to the 'country' column
movies_df["country"] = movies_df["country"].apply(process_countries)

# Step 3: Split the strings by ", " and get unique countries using a set
all_countries = movies_df["country"].str.split(", ").explode().unique()

# Step 4: Count the unique countries
n_countries = len(all_countries)

# Print the result
f"There are {n_countries} different countries in the data"

# Step 1: Create a new column with the length of each title
movies_df['title_length'] = movies_df['title'].apply(lambda x: len(x))

# Step 2: Calculate the average title length
avg_title_length = movies_df['title_length'].mean()

# Print the result
f"The average title length is {avg_title_length} characters"

# Ex 2.7: Line chart of the average duration of movies (not TV shows) for every year

# Step 1: Filter out TV shows (assume the 'type' column distinguishes between movies and TV shows)
movies_df_movies = movies_df[movies_df['type'] == 'Movie']

# Step 2: Create a new column for the movie duration in minutes
# We assume that the 'duration' column has the format "XX min"
movies_df_movies['duration_minutes'] = movies_df_movies['duration'].apply(lambda x: int(x.split()[0]) if isinstance(x, str) else None)

# Step 3: Group by year and calculate the average duration for each year
movies_avg_duration_per_year = movies_df_movies.groupby('release_year')['duration_minutes'].mean()

# Step 4: Plot the line chart
fig = plt.figure(figsize=(9, 6))

plt.plot(movies_avg_duration_per_year.index, movies_avg_duration_per_year, marker='o', linestyle='-', color='b')
plt.title("Average Duration of Movies Across Years")
plt.xlabel("Year")
plt.ylabel("Average Duration (minutes)")

st.pyplot(fig)