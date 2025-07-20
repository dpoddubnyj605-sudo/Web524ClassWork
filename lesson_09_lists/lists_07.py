# cinema_genres = ["Drama", "Comedy", "Fantasy", "Action"]
# cinema_genres[1] = 'Scy-Fy'
# print(cinema_genres)
#
# # slices/срезы
# cinema_genres = ["Drama", "Comedy", "Fantasy", "Action", "Scy-Fy", "Horror"]
# cinema_genres_slice = cinema_genres[2:4]
# print(cinema_genres_slice)
# cinema_genres_slice_from_beginning = cinema_genres[:4]
# print(cinema_genres_slice_from_beginning)
# cinema_genres_slice_till_end = cinema_genres[2:]
# print(cinema_genres_slice_till_end)
# cinema_genres_slice_step = cinema_genres[::2]
# print(cinema_genres_slice_step)
# cinema_genres_slice_step = cinema_genres[1:5:2]
# print(cinema_genres_slice_step)
# cinema_genres_slice_all = cinema_genres[:]
# print(cinema_genres_slice_all)
print()

# # оператор принадлежности in
# cinema_genres = ["Drama", "Comedy", "Fantasy", "Romance", "Comedy"]
# print("Drama" in cinema_genres)
# print("Detective" in cinema_genres)
# print()
#
# my_genre = "Drama"
# if my_genre in cinema_genres:
#     print(my_genre)
# else:
#     print('Жанра нет в списке')

# del
cinema_genres = ["Drama", "Comedy", "Fantasy", "Romance", "Comedy"]
del cinema_genres[2]
print(cinema_genres)

