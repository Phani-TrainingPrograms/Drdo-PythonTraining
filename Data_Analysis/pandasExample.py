import pandas as pd
import numpy as np
# Pandas stand for Python Data Analysis, a library for analysing, cleaning, exploring and
# manipulating the data.
# Used to analyse big data and make conclusions based on statistical theories.
# Used to perform data centric operations which is part of data sciences.
# Its open source and its code is available in Github.

df = pd.read_csv("imdb_top_1000.csv")

# print(df)
#
# data = df.to_numpy()
# print("Data Shape: ", data.shape)
#
# print("First 5 rows: ", data[:5])

# If U have data in the form of rows and columns, we call that as DataFrames.
# my_set = {
#     'Cars' : ["Honda", "Maruti", "Hyndai", "Toyota"],
#     "ratings" : [7, 9, 6, 9]
# }
#
# my_df = pd.DataFrame(my_set)
# print(my_df)

# Single Dimensional Arrays are called as Series.
# data = pd.Series([10,12,14,15,16])
# print(data)

#########Extracting columns#########################################
# imdb_ratings = df['IMDB_Rating'].to_numpy()
# votes = df['No_of_Votes'].to_numpy()
# print(imdb_ratings[:10], votes[:10])
#
# min_rating = np.min(imdb_ratings)
# max_rating = np.max(imdb_ratings)
#
# print(f"Rating is b/w {min_rating} and {max_rating}")
#
# # Display top rated movies:
# top_ratings = imdb_ratings > 8
# top_movies = df['Series_Title'][top_ratings]
# print(top_movies[:5])
#
# #Find top 10 Movies with max no votes:
# top_ten = np.argsort(votes)[-10:]
# top_5_movies = df.iloc[top_ten]
# print("Top 10: \n", top_5_movies[['Series_Title', 'No_of_Votes', 'Director']])
#
# #Find the max no of movies released based on Year,
# movies_per_year = df.groupby('Released_Year').size()
# max_year = movies_per_year.idxmax() # returns the index of the max value.
# max_count = movies_per_year.max() # Gets the max value.
# print(f"In the year of {max_year}, {max_count} no of movies were released")
#
#
# # Get the Top 5 directors with max no of movies:
# # Get the no of movides directed by each director
# movies_per_director = df.groupby('Director').size();
#
# # sort and get the top 5.
# top_5_directors = movies_per_director.sort_values(ascending=False).head(10) # head refers to the
# # key on which the grouping is done, in this case, the director.
# print(top_5_directors)
#
# # Get Unique years:
# unique_years = df['Released_Year'].unique()
# print(unique_years)

# Display actors of Top rated movies that has rating more than 8.
high_rated = df[df['IMDB_Rating'] > 8.5]['Star1']
print(high_rated)

# Find the highest Gross Movie:
max_gross = df[df["Gross"] == df["Gross"].max()]

print(max_gross['Series_Title'])

# Find the highest no of actor-director collaborations:



