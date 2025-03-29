import csv
from istorage import IStorage

class StorageCsv(IStorage):
    def __init__(self, filename):
        self.filename = filename
        self.movies = self.load()

    def load(self):
        try:
            with open(self.filename, mode='r', newline='') as file:
                reader = csv.DictReader(file)
                return [row for row in reader]
        except FileNotFoundError:
            return []
        except csv.Error:
            return []

    def save(self):
        with open(self.filename, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=["title", "year", "rating", "poster"])
            writer.writeheader()
            writer.writerows(self.movies)

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
