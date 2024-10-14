Movie Collection Web Application
This project is a backend web application that allows users to create collections of movies they like, using a third-party movie listing API and JWT authentication. The application also implements a request counting middleware for monitoring API usage.

1.Technologies Used
 Backend: Django
 Authentication: JWT (JSON Web Token)
 Database: SQLite3
 External API Integration: Movie listing API (with basic auth and retry mechanism)
 Cache: Django cache framework (used for request counter)

2.Setup
1. Download and Install Python
Ensure Python 3.9 or above is installed on your system.

2. Django Project Creation
   First, ensure you have Django installed: pip install django
   Create a Django project named movie_collection:
   django-admin startproject movie_collection
   cd movie_collection
   Django App Creation
   Inside your Django project, create a new app for managing movies:
   python manage.py startapp movies

3. Set Up Virtual Environment
pip install virtualenv
virtualenv env
Activate the environment: env\Scripts\activate

4. Install Requirements : pip install -r requirements.txt

5. Set Up Environment Variables
Create a .env file in the project root with the following content:
API_USERNAME=<your_api_username>
API_PASSWORD=<your_api_password>

6. Run Database Migrations
python manage.py makemigrations
python manage.py migrate

7. Create a Superuser (Admin) : python manage.py createsuperuser

8. Run the Server: python manage.py runserver
Visit application at http://127.0.0.1:8000.

API Endpoints

Authentication Endpoints
1.Register: POST /api/register/
2.Login: POST /api/login/
3.Token Refresh: POST /api/token/refresh/

Movie Endpoints
1.Fetch Movies: GET /api/movies/

Collection Endpoints
1.Create Collection: POST /api/collection/
2.View Collections: GET /api/collection/
3.View Collection Details: GET /api/collection/<collection_uuid>/
4.Update Collection: PUT /api/collection/<collection_uuid>/
5.Delete Collection: DELETE /api/collection/<collection_uuid>/

Request Counter Endpoints
1.Get Request Count: GET /api/request-count/
2.Reset Request Count: POST /api/request-count/reset/

Testing
Tests for the project have been implemented to ensure the key functionalities:
1.User registration and authentication.
2.Movie listing.
3.CRUD operations for movie collections.
4.Request counter functionality.
To run the tests:python manage.py test

Best Practices Followed
The project follows PEP8 coding standards.
Use of environment variables for sensitive information like API credentials.
Clean, modular code with most business logic moved outside the views.
Proper exception handling across the application.

Features

1.User Authentication
 JWT-based authentication using rest_framework_simplejwt.
 Users can register, log in, and obtain tokens for authenticated API requests.
 Movie Collection Management

2.Users can create, update, view, and delete collections of movies.
 Each user can have multiple collections with different movies.
 API integration with a third-party movie listing service for fetching movie data.
 Users can fetch movies, view a collection, and manage their collections.

3.Request Counter Middleware
 A custom middleware to count the number of requests made to the server.
 APIs to get the current request count and reset it.








