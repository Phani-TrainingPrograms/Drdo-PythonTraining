import MovieRepo as movieRepo
from Movie import Movie
movieDb = movieRepo.MovieRepository("demo.csv")

def get_movie_details():
    id = int(input("Enter the MovieID: "))
    title = input("Enter the Title: ")
    director = input("Enter the Director Name: ")
    year = input("Enter the Year of Release: ")
    movie = Movie(id, title, director, year)
    return movie

add_feature = lambda movie : movieDb.add_movie(movie)


update_feature = lambda movie : movieDb.update_movie(movie.id, movie)


def select_feature():
    title = (input("Enter the Title of the movie to search"))
    found = movieDb.get_movie_detail(title)
    if not found:
        print("No movie found to display")
    else:
        print(found)

def view_all_feature():
    movies = movieDb.list_movies()
    if not movies:
        print("No Movies are available")
    else:
        for m in movies:
            print(m)

choice = input("Enter the choice: [1-4]")
match choice:
    case "1":
        new_movie = get_movie_details()
        add_feature(new_movie)
    case "2":
        view_all_feature()
    case "3":
        print("Enter the Details of the movie for updating")
        updating_movie = get_movie_details()
        update_feature(updating_movie)
    case "4":
        select_feature()
    case _:
        print("Invalid Choice, Please try again!!!")

####TODO:
'''
Provide a Decorator for creating lines b/w each feature that is displayed on the UI
Maintain a While Loop for the App to run continuously
Application should not terminate abnormally.
All kinds of Exception handling should be done. 
'''