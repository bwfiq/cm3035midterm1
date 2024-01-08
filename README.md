**README.md**

# Django Movie Database

## Packages and Versions

- Django: 5.0.1
- Django REST Framework: 3.14.0

To install the required packages, run:

```bash
pip install -r requirements.txt
```

## Development Environment

- Operating System: Windows 10
- Python Version: 3.12.1

## Django Admin Site

To log in to the Django Admin site:

1. Start the development server:

   ```bash
   python manage.py runserver
   ```

2. Open a web browser and navigate to [http://localhost:8000/admin/](http://localhost:8000/admin/)

3. Log in with the following credentials:

   - Username: admin
   - Password: 1234

## URLs

### Project-Level URLs (`cm3035midterm1/urls.py`):

- Home: [http://localhost:8000/](http://localhost:8000/)
- Admin: [http://localhost:8000/admin/](http://localhost:8000/admin/)
- MovieDB App: [http://localhost:8000/movieDB/](http://localhost:8000/movieDB/)

### App-Level URLs (`movieDB/urls.py`):

- Movie List: [http://localhost:8000/movieDB/](http://localhost:8000/movieDB/)
- Movie List/Create: [http://localhost:8000/movieDB/movies/](http://localhost:8000/movieDB/movies/)
- Movie Detail: [http://localhost:8000/movieDB/movies/{id}/](http://localhost:8000/movieDB/movies/{id}/)
- Top Downloads: [http://localhost:8000/movieDB/top-downloads/](http://localhost:8000/movieDB/top-downloads/)
- Longest Movies: [http://localhost:8000/movieDB/movies/longest/](http://localhost:8000/movieDB/movies/longest/)
- Shortest Movies: [http://localhost:8000/movieDB/movies/shortest/](http://localhost:8000/movieDB/movies/shortest/)
- Add Movie: [http://localhost:8000/movieDB/add-movie/](http://localhost:8000/movieDB/add-movie/)
- Update Movie: [http://localhost:8000/movieDB/movies/update/{id}/](http://localhost:8000/movieDB/movies/update/{id}/)

## Unit Tests

Run unit tests using the following command:

```bash
python manage.py test
```

## Data Loading Script

The data loading script is a Django management command named `load_data`. To execute this command and load data from a CSV file into the database:

```bash
python manage.py import_movies --file=movie_dataset.csv
```

## Additional Information

- The main application is located in the `movieDB` directory.
- The Django project settings are in the `cm3035midterm1` directory.
