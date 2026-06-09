import requests
import random

API_KEY = "619ae3b14caa6f3fc0b41ba499aa2132"
BASE = "https://api.themoviedb.org/3"

genres_resp = requests.get(
    f"{BASE}/genre/movie/list",
    params={"api_key": API_KEY, "language": "en-US"}
)
genres = genres_resp.json()["genres"]
genre_map = {g["name"].lower(): g["id"] for g in genres}

print("Available genres:", ", ".join(g["name"] for g in genres))
choice = input("Pick a genre: ").strip().lower()

if choice not in genre_map:
    print("Genre not found.")
else:
    movies_resp = requests.get(
        f"{BASE}/discover/movie",
        params={
            "api_key": API_KEY,
            "with_genres": genre_map[choice],
            "sort_by": "popularity.desc"
        }
    )
    movies = movies_resp.json()["results"]

    if movies:
        movie = random.choice(movies)
        print(f"\nRecommended: {movie['title']} ({movie.get('release_date', 'N/A')[:4]})")
        print(f"Rating: {movie['vote_average']}/10")
        print(f"Overview: {movie['overview']}")
    else:
        print("No movies found.")