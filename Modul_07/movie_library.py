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
Number of views: {self.view_count}
'''
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
S{self.season:02}E{self.episode:02}
'''

    def __repr__(self):
        return f'''{super().__repr__()}
S{self.season.rjust(2, "0")}E{self.episode:02}
'''


def get_film_data(title):
    response = requests.get(f'http://www.omdbapi.com/?apikey=74a6ab0e&'
                            f't={title}')
    film_data = json.loads(response.text)
    if film_data['Response'] == 'False':
        film_data = False
    print(film_data)

    return film_data


def generate_one_series():
    pass


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
