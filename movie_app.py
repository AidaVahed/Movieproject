import random
import requests
from fuzzywuzzy import process
from colorama import Fore, init

init(autoreset=True)


class MovieApp:
    def __init__(self, storage, api_key):
        self._storage = storage
        self._api_key = api_key

    def list_movies(self):
        movies = self._storage.list_movies()
        if not movies:
            print("Error: Missing movie data.")
            return

        print(f"{len(movies)} movies in total:")
        for movie in movies:
            print(
                f"Title: {movie['title']}, Year: {movie['year']}, Rating: {movie['rating']}, Poster: {movie['poster']}")

    def get_movie_data_from_api(self, title):
        # Make the API request here
        url = f"https://www.omdbapi.com/?t={title}&apikey={self._api_key}"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            if data['Response'] == 'True':
                return {
                    'title': data['Title'],
                    'year': data['Year'],
                    'rating': data['imdbRating'],
                    'poster': data['Poster']
                }
            else:
                print("Movie not found.")
                return None
        else:
            print("Error fetching movie data from API.")
            return None

    def add_movie(self):
        title = input("Enter movie title: ").strip()
        if not title:
            print("Title cannot be empty.")
            return

        movie_data = self.get_movie_data_from_api(title)
        if movie_data:
            self._storage.add_movie(
                movie_data['title'],
                movie_data['year'],
                movie_data['rating'],
                movie_data['poster']
            )
            print(f"Movie '{movie_data['title']}' added successfully!")
        else:
            print("Failed to fetch movie data.")

    def delete_movie(self):
        title = input(Fore.MAGENTA + "Enter movie title to delete: ")
        self._storage.delete_movie(title)
        print(Fore.GREEN + f"Movie '{title}' deleted successfully!")

    def update_movie(self):
        title = input(Fore.MAGENTA + "Enter movie title to update: ")
        year = input(Fore.MAGENTA + "Enter new year: ")
        rating = input(Fore.MAGENTA + "Enter new rating: ")
        poster = input(Fore.MAGENTA + "Enter new poster URL: ")

        self._storage.update_movie(title, year, rating, poster)
        print(Fore.GREEN + f"Movie '{title}' updated successfully!")

    def stats(self):
        movies = self._storage.list_movies()
        if not movies:
            print(Fore.RED + "No movies available to analyze.")
            return

        ratings = [float(movie["rating"]) for movie in movies]
        average = sum(ratings) / len(ratings)
        print(Fore.CYAN + f"Average rating: {average:.2f}")

    def random_movie(self):
        movies = self._storage.list_movies()
        if not movies:
            print(Fore.RED + "No movies available for random selection.")
            return

        movie = random.choice(movies)
        print(Fore.CYAN + f"Random Movie: {movie['title']} ({movie['year']}), Rating: {movie['rating']}")

    def search_movie(self):
        search_query = input(Fore.MAGENTA + "Enter search term: ")
        movies = self._storage.list_movies()
        if not movies:
            print(Fore.RED + "No movies available to search.")
            return

        results = process.extract(search_query, [movie["title"] for movie in movies], limit=5)
        print(Fore.CYAN + f"Search results for '{search_query}':")
        for result in results:
            print(Fore.YELLOW + f"Title: {result[0]}")

    def sort_movies_by_rating(self):
        movies = self._storage.list_movies()
        if not movies:
            print(Fore.RED + "No movies available to sort.")
            return

        sorted_movies = sorted(movies, key=lambda x: float(x["rating"]), reverse=True)
        print(Fore.CYAN + "Movies sorted by rating:")
        for movie in sorted_movies:
            print(Fore.YELLOW + f"Title: {movie['title']}, Year: {movie['year']}, Rating: {movie['rating']}")

    def generate_website(self):
        movies = self._storage.list_movies()
        if not movies:
            print(Fore.RED + "No movies available to generate website.")
            return

        website_content = self.create_website_content(movies)

        with open("_static/index.html", "w") as file:
            file.write(website_content)

        print(Fore.GREEN + "Website was generated successfully!")

    def create_website_content(self, movies):
        template = self.get_template()

        title = "My Movie App"
        movie_grid = self.create_movie_grid(movies)

        website_content = template.replace("__TEMPLATE_TITLE__", title)
        website_content = website_content.replace("__TEMPLATE_MOVIE_GRID__", movie_grid)

        return website_content

    def get_template(self):
        template = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>__TEMPLATE_TITLE__</title>
            <link rel="stylesheet" href="style.css">
        </head>
        <body>
            <h1>Welcome to __TEMPLATE_TITLE__</h1>
            <div class="movie-grid">
                __TEMPLATE_MOVIE_GRID__
            </div>
        </body>
        </html>
        """
        return template

    def create_movie_grid(self, movies):
        grid = ""
        for movie in movies:
            grid += f"""
            <div class="movie-card">
                <img src="{movie['poster']}" alt="{movie['title']} Poster">
                <h2>{movie['title']}</h2>
                <p>Year: {movie['year']}</p>
                <p>Rating: {movie['rating']}</p>
            </div>
            """
        return grid

    def run(self):
        while True:
            print(Fore.BLUE + "\n********** My Movies Database **********")
            print(Fore.CYAN + "1. List movies")
            print(Fore.CYAN + "2. Add movie")
            print(Fore.CYAN + "3. Delete movie")
            print(Fore.CYAN + "4. Update movie")
            print(Fore.CYAN + "5. Stats")
            print(Fore.CYAN + "6. Random movie")
            print(Fore.CYAN + "7. Search movie")
            print(Fore.CYAN + "8. Movies sorted by rating")
            print(Fore.CYAN + "9. Generate Website")
            print(Fore.RED + "0. Exit")

            choice = input(Fore.MAGENTA + "Enter choice (0-9): ").strip()

            if choice == "1":
                self.list_movies()
            elif choice == "2":
                self.add_movie()
            elif choice == "3":
                self.delete_movie()
            elif choice == "4":
                self.update_movie()
            elif choice == "5":
                self.stats()
            elif choice == "6":
                self.random_movie()
            elif choice == "7":
                self.search_movie()
            elif choice == "8":
                self.sort_movies_by_rating()
            elif choice == "9":
                self.generate_website()
            elif choice == "0":
                print(Fore.GREEN + "Bye!")
                break
            else:
                print(Fore.RED + "Invalid choice. Try again.")

            input(Fore.MAGENTA + "Press Enter to continue...")
