#movie class with the attributes: id, title, director, year
class Movie:
    def __init__(self, id, title, director, year):
        self.id = id
        self.title = title
        self.director = director
        self.year = year

    def __str__(self):
        return f"Id: {self.id}, Title: {self.title}, Director : {self.director}, Releasing Year: {self.year}"