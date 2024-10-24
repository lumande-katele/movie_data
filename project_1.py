
# Importing the necessary libraries
import pandas as pd

# Reading the CSV file
movie_data = pd.read_csv("movie_dataset.csv")

# Seing the information about our dataset
movie_data.info()

# Summary statistics of the dataset
print(movie_data.describe())

# Droping the rows with missing values (without using inplace)
movie_data_clean = movie_data.dropna(axis=0, how="any")

# Checking if there are any missing values after dropping
print(movie_data_clean.isnull().sum())

# Droping duplicate rows (modifying the DataFrame in place)
movie_data_clean.drop_duplicates(inplace=True)

# Sorting the DataFrame by 'Rating' column in ascending order and display the top 5 rows
df_sorted = movie_data_clean.sort_values(by='Rating', ascending=False)

# Display the first 5 rows of the sorted DataFrame
print(df_sorted.head())

# Calculating the mean revenue from the cleaned dataset
mean_revenue = movie_data_clean["Revenue (Millions)"].mean()
print(f"Mean Revenue: {mean_revenue}")

# Filtering for movies from the year 2016
movie = movie_data[movie_data["Year"] == 2016]

print(movie)
unique = movie_data
# Correcting filtering for the years 2015, 2016, and 2017 using the original movie_data
filtered_data = movie_data[movie_data["Year"].isin([2015, 2016, 2017])]
print(filtered_data)

# Calculating the total sum of 'Revenue (Millions)' for the filtered data
sum_the_values = filtered_data["Revenue (Millions)"].mean()
print(sum_the_values)

total_revenue = movie_data_clean["Revenue (Millions)"].mean()
print(total_revenue)


movies_nolan = movie_data[movie_data["Director"] == "Christopher Nolan"]
print(len(movies_nolan))

movies_rating = movie_data[movie_data["Rating"] >= 8]

print(len(movies_rating ))

print(movies_nolan["Rating"].median())

print(movie_data.groupby("Year")["Rating"].mean().max())

movies_2006 = movie_data[movie_data["Year"]==2006]
print(len(movies_2006))

num_movies_2006 = len(movies_2006)
print(num_movies_2006)

movies_2016 = movie_data[movie_data["Year"]==2016]
num_movies_2016 = len(movies_2016)
print(num_movies_2016 )

movies_percent_increase = ((num_movies_2016-num_movies_2006)/num_movies_2006)*100
print(movies_percent_increase)

# Importing Counter from collections module
from collections import Counter
# Assuming actor names are separated by commas
all_actors = movie_data["Actors"].str.cat(sep=',').split(',')

#Clean up whitespace and create a Counter object to count occurrences of each actor
all_actors = [actor.strip() for actor in all_actors]  # Remove extra whitespace
actor_counts = Counter(all_actors)

# Step 5: Find the most common actor and their count
most_common_actor, most_common_count = actor_counts.most_common(1)[0]

# Step 6: Print the results
print(f"The most common actor is: {most_common_actor} with {most_common_count} appearances.")

# Split the genres by comma, explode the lists into separate rows, and get unique values
unique_genres = movie_data['Genre'].str.split(',').explode().str.strip().unique()

# Get the count of unique genres
unique_genre_count = len(unique_genres)

# Print the count of unique genres
print(f"There are {unique_genre_count} unique genres in the dataset.")

















