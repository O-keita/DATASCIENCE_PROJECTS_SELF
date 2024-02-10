import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
netflix_movies = pd.read_csv('/home/omar/coding/DATASCIENCE/DATASCIENCE_PROJECTS_SELF/NETFLIX_MOVIES/netflix_titles.csv')

# Select only movies (exclude TV shows)
movies = netflix_movies[netflix_movies['type'] == 'Movie']

# Extract relevant columns
selected_movies = movies[['title', 'release_year', 'duration', 'listed_in']]

# Convert 'duration' to numeric (assuming it's in string format)
selected_movies['duration'] = pd.to_numeric(selected_movies['duration'].str.replace(' min', '', regex=False), errors='coerce')
colors =[]
for label, row in selected_movies.iterrows():

    if row['listed_in'] == 'Documentaries':
        colors.append('red')

    elif row['listed_in'] == 'Comedies':
        colors.append('green')

    elif row['listed_in'] == 'Dramas':
        colors.append('blue')

    elif row['listed_in'] == 'Thrillers':
        colors.append('pink')

    elif row['listed_in'] == 'Action':
        colors.append('violet')

    else:
        colors.append('black')


# Scatter plot
plt.scatter(selected_movies['release_year'], selected_movies['duration'], c=colors)

# Set labels and title
plt.title("Netflix Movies over the Years with Durations")
plt.xlabel("Release Year")
plt.ylabel("Duration (minutes)")

# Show the plot
plt.show()
