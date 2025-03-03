# Django Movie Recommendation System

## Overview
This project is a web-based movie recommendation system built with Django that suggests similar movies based on content features. It leverages the TMDB API to fetch movie details and displays recommendations with movie posters, taglines, and overviews.

## Features
- Movie recommendation based on content similarity
- Search functionality for movies
- Persistent storage of recommendations using Django models
- Movie detail pages with poster images, taglines, and overviews
- Session-based caching to improve performance and reduce API calls

## Technical Stack
- **Backend**: Django (Python)
- **Database**: SQLite3
- **External API**: TMDB (The Movie Database)
- **Frontend**: HTML/CSS (Django templates)

## Project Structure
- **Models**: `Movies` model for storing movie recommendations
- **Views**: Functions for handling requests and rendering templates
- **Templates**: HTML templates for displaying movie data

## Installation

### Prerequisites
- Python 3.x
- Django
- requests library

### Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/django-movie-recommendation.git
   cd django-movie-recommendation
   ```

2. Install dependencies:
   ```bash
   pip install django requests
   ```

3. Set up the database:
   ```bash
   python manage.py migrate
   ```

4. Load the movie recommendation data:
   ```bash
   python manage.py loaddata movies.json
   ```
   
5. Run the development server:
   ```bash
   python manage.py runserver
   ```

6. Access the application at http://127.0.0.1:8000/

## Usage

### Home Page
The home page provides a search box where users can enter a movie name to get recommendations.

### Recommendation Page
After searching for a movie, users are redirected to the recommendation page that displays:
- The searched movie with its poster
- A list of recommended movies with their posters

### Movie Details
Users can click on any movie to view additional details including:
- Movie title
- Movie poster
- Tagline
- Overview
- Release date

## How It Works

### Data Flow
1. User searches for a movie by name
2. System looks up the movie in the database
3. If found, retrieves associated movie IDs for recommendations
4. Fetches movie details from TMDB API for each ID
5. Displays results to the user
6. Caches results in the session for future requests

### Caching Strategy
- Movie details are stored in the session to minimize API calls
- Once a movie is searched, its recommendations are cached for the session duration
- The current movie is tracked to provide recommendations even with empty searches

## API Integration
The system uses TMDB API to fetch movie details including:
- Movie titles
- Poster images
- Taglines
- Overviews
- Release dates

## Database Schema
The `Movies` model stores:
- `key`: Movie name (lowercase)
- `value1` to `value6`: Movie IDs for the searched movie and its recommendations

## Security Notes
- The API key in the code should be replaced with an environment variable for production use
- The session data should be regularly cleaned to prevent memory issues

## Future Improvements
- Implement user accounts and personalized recommendations
- Add pagination for movies with many recommendations
- Create an admin interface for managing movie data
- Implement advanced search filters (by genre, year, etc.)
- Add responsive design for mobile devices
