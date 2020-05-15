from movie_library import generate_film, get_movies, get_series, search_title,\
    run_views, top_titles, add_full_series

library = generate_film(10)

print(library)

library = run_views(library, 10)

print(f'List of movies only: {get_movies(library)}')

print(f'List of series only: {get_series(library)}')

print(search_title(library, 'Pulp Fiction'))

print(top_titles(library, 5, 0))  # print 5 most viewed picture

print(top_titles(library, 2, 1))  # print 2 most viewed movies

print(top_titles(library, 2, 2))  # print 2 most viewed series

library.append(add_full_series('The Sopranos', library, 10))

print(library)
