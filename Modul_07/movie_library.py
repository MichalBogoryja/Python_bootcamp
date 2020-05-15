import requests
import json
import random

class Movie:
    def __init__(self, title, year, genre):
        self.title = title
        self.year = year
        self.genre = genre

        # Variables
        self.view_count = 0

    def __str__(self):
        text = f'''Title: {self.title}
Year: {self.year}
Genre: {self.genre}
Number of views: {self.view_count}'''
        return text

    def __repr__(self):
        text = f'''

Title: {self.title}
Year: {self.year}
Genre: {self.genre}
Number of views: {self.view_count}'''
        return text

    def play(self):
        self.view_count += 1


class Series(Movie):
    def __init__(self, season, episode, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.season = season
        self.episode = episode

    def __str__(self):
        return f'''{super().__str__()}
S{self.season.rjust(2, "0")}E{self.episode:02}'''

    def __repr__(self):
        return f'''{super().__repr__()}
S{self.season.rjust(2, "0")}E{self.episode:02}'''


def get_film_data(title):
    response = requests.get(f'http://www.omdbapi.com/?apikey=74a6ab0e&'
                            f't={title}')
    film_data = json.loads(response.text)
    if film_data['Response'] == 'False':
        film_data = False
    # print(film_data)

    return film_data


def generate_film(number):
    film = []
    m = open('movie_list.txt')
    s = open('series_list.txt')
    for i in range(number):
        check = random.randint(0, 1)
        if check == 1:
            title = m.readline().replace('\n', '')
        else:
            title = s.readline().replace('\n', '')
        film_data = get_film_data(title)
        if not film_data:
            film.append(f'\nMovie {title} doesnt exist')
        elif film_data['Type'] == 'movie':
            film.append(Movie(title, film_data['Year'], film_data['Genre']))
        else:
            film.append(Series(title=title,
                               year=film_data['Year'],
                               genre=film_data['Genre'],
                               season=film_data['totalSeasons'],
                               episode=1))
    return film


def check_series(series, library):
    for i in range(len(library)-1):
        if series in library[i].title and isinstance(library[i], Series):
            series = library[i]
            break
        else:
            if i == len(library) - 2:
                text = "There is no such a series"
                raise Exception(text)

    return series


def add_full_series(series, library, episodes):
    entire_series = []
    series = check_series(series, library)

    for season in range(int(series.season)):
        for i in range(1, episodes+1):
            entire_series.append(Series(title=series.title,
                                        year=series.year,
                                        genre=series.genre,
                                        season=str(season),
                                        episode=i))

    return entire_series


def get_movies(full_list):
    sorted_list = []
    for picture in full_list:
        if isinstance(picture, Movie) and not isinstance(picture, Series):
            sorted_list.append(picture)

    return sorted_list


def get_series(full_list):
    sorted_list = []
    for picture in full_list:
        if isinstance(picture, Series):
            sorted_list.append(picture)

    return sorted_list


def search_title(library, name):
    for picture in library:
        if picture.title == name:
            text = "This film is on the list"
            break
        else:
            text = "This film is not on the list"

    return text


def generate_views(library):
    film = random.randint(0, len(library)-1)
    views = random.randint(1, 100)
    library[film].view_count += views

    return library


def run_views(library, times):
    for i in range(0, times):
        generate_views(library)

    return library


def top_titles(library, items, movies):
    if movies == 0:
        pass
    elif movies == 1:
        library = get_movies(library)
    elif movies == 2:
        library = get_series(library)

    sorted_library = sorted(library, key=lambda picture: picture.view_count,
                            reverse=True)
    sorted_library = sorted_library[:items]

    return sorted_library

