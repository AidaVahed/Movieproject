# Movie Database Project

## Project Overview

The **Movie Database Project** is a Python application designed to allow users to manage a collection of movies. The application supports adding, listing, updating, and deleting movies. It also provides functionalities to search, sort by rating, generate statistics, and display movies in a grid format on a simple website. The project stores movie data in either a **JSON** or **CSV** file.

## Features

- **Add Movies**: Fetch movie information from an external API (e.g., OMDB API) by entering the movie title.
- **List Movies**: View all movies stored in the database.
- **Update Movies**: Modify movie details such as year, rating, and poster.
- **Delete Movies**: Remove a movie from the database.
- **Search Movies**: Search for movies by title.
- **Movies Sorted by Rating**: List movies sorted by their rating.
- **Generate Website**: Generates a simple webpage showcasing all the movies in a grid layout.
- **Statistics**: Provides basic statistics about the movies stored in the database.

## Project Structure

- **`main.py`**: Entry point for the application. It initializes and runs the application.
- **`movie_app.py`**: Contains the main logic for interacting with movies.
- **`storage_json.py`**: Handles storing and loading movies in a JSON file.
- **`storage_csv.py`**: Handles storing and loading movies in a CSV file.
- **`istorage.py`**: Interface for storage classes (JSON/CSV).
- **`index_template.html`**: Template for generating the movie website.
- **`styles.css`**: Styles for the generated movie website.

## Requirements

This project requires Python 3.7+ and the following dependencies:

- `requests`: For fetching movie data from external APIs.
- `colorama`: For colored terminal output.

## Setup

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/movie-database.git
cd movie-database
