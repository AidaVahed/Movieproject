from movie_app import MovieApp
from storage_json import StorageJson
from storage_csv import StorageCsv

def main():
    storage_type = "csv"
    api_key = "ea225778"

    if storage_type == "json":
        storage = StorageJson("movies.json")
    elif storage_type == "csv":
        storage = StorageCsv("movies.csv")
    else:
        print("Invalid storage type.")
        return


    app = MovieApp(storage, api_key)

    app.run()

if __name__ == "__main__":
    main()
