import json
from istorage import IStorage

class StorageJson(IStorage):
    def __init__(self, filename):
        self.filename = filename
        self.movies = self.load()

    def load(self):
        try:
            with open(self.filename, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return []
        except json.JSONDecodeError:
            return []

    def save(self):
        with open(self.filename, 'w') as file:
            json.dump(self.movies, file, indent=4)

    def list_movies(self):
        return self.movies

    def add_movie(self, title, year, rating, poster):
        self.movies.append({
            "title": title,
            "year": year,
            "rating": rating,
            "poster": poster
        })
        self.save()

    def delete_movie(self, title):
        self.movies = [movie for movie in self.movies if movie["title"] != title]
        self.save()

    def update_movie(self, title, year, rating, poster):
        for movie in self.movies:
            if movie["title"] == title:
                movie["year"] = year
                movie["rating"] = rating
                movie["poster"] = poster
                self.save()
                break
