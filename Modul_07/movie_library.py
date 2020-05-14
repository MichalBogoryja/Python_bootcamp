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


class Series(Movie):
    def __init__(self, season, episode, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.season = season
        self.episode = episode

    def __str__(self):
        return f'''{super().__str__()} \
Season: {self.season}
Episode: {self.episode}
'''


def play(film):
    film.view_count += 1


shrek = Movie("Shrek", "2008", "Kids")
twin_peaks = Series(title="Twin Peaks", year="1990", genre="Drama", season="1", episode="04")
play(shrek)
play(twin_peaks)

print(shrek)
print(twin_peaks)
