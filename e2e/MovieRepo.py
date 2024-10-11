# This class represents the Repository of the movies on which we can perform CURD operations
import csv
from Movie import Movie

class MovieRepository:
    def __init__(self, file_name):
        self.filename = file_name

    def add_movie(self, movie):
        with open(self.filename, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([movie.id, movie.title, movie.director, movie.year])
            print(f"Movie details added successfully!!!")

    def list_movies(self):
        movies = []
        try:
            with open(self.filename, 'r', newline='') as file:
                reader = csv.reader(file)
                for row in reader:
                    movies.append(Movie(int(row[0]),row[1],row[2],row[3]))
        except FileNotFoundError as ferr:
            print(f"File Not found: {ferr}")
        else:
            print("The Total movies: ", len(movies))
            return movies

    def update_movie(self, movie_id, modified_movie):
        movies = self.list_movies()
        updated = False
        with open(self.filename, 'w', newline='') as file:
            writer = csv.writer(file)
            for movie in movies:
                if movie.id == str(movie_id):
                    writer.writerow([modified_movie.id, modified_movie.title,
                                     modified_movie.director, modified_movie.year])
                    updated = True
                    print("Updated Successfully")
                else:
                    writer.writerow([movie.id, movie.title, movie.director, movie.year])
        if not updated:
            print(f"Movie not found to update!!!")

    def get_movie_detail(self, movie_title):
        movies = self.list_movies()
        temp = list(filter(lambda movie : movie.title == movie_title, movies))
        return temp[0]
