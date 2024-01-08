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
