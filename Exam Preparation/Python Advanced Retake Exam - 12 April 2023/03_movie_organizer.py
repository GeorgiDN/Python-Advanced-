def movie_organizer(*args):
    movies_data = {}
    for movie_info in args:
        movie_name = movie_info[0]
        genre = movie_info[1]
        if genre not in movies_data:
            movies_data[genre] = []
        movies_data[genre].append(movie_name)

    result = ''
    sorted_movie_data = dict(sorted(movies_data.items(), key=lambda x: (-len(x[1]), x[0])))
    for genre, movies in sorted_movie_data.items():
        sorted_movies = sorted(movies)
        result += f"{genre} - {len(movies)}\n"
        for movie in sorted_movies:
            result += f"* {movie}\n"

    return result.strip()


# print(movie_organizer(
#     ("The Matrix", "Sci-fi")))
#
#
# print(movie_organizer(
#     ("The Godfather", "Drama"),
#     ("The Hangover", "Comedy"),
#     ("The Shawshank Redemption", "Drama"),
#     ("The Pursuit of Happiness", "Drama"),
#     ("The Hangover Part II", "Comedy")))
#
#
# print(movie_organizer(
#     ("Avatar: The Way of Water", "Action"),
#     ("House Of Gucci", "Drama"),
#     ("Top Gun", "Action"),
#     ("Ted", "Comedy"),
#     ("Duck Soup", "Comedy"),
#     ("The Dark Knight", "Action"),
#     ("A Star Is Born", "Musicals"),
#     ("The Warrior", "Action"),
#     ("Like A Boss", "Comedy"),
#     ("The Green Mile", "Drama"),
#     ("21 Jump Street", "Comedy")))


