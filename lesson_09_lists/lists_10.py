import random

cinema_genres = ["Drama", "Comedy", "Fantasy", "Comedy", "Romance"]
print(cinema_genres)
random.shuffle(cinema_genres)
print(cinema_genres)

cinema_genres = ["Drama", "Comedy", "Fantasy", "Romance", "Scy-Fy"]
genres_sample = random.sample(cinema_genres, 3)
print(genres_sample)

# some_str = "Привет! Я строка."
# sample_str = random.sample(some_str, len(some_str))
# print(sample_str)
# result = ''.join(sample_str)
# print(result)

cinema_genres = ["Drama", "Comedy", "Fantasy", "Romance", "Scy-Fy"]
my_genre = random.choice(cinema_genres)
print(my_genre)
