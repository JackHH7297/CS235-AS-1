from domainmodel.movie import Movie
from random import Random
import random

class WatchList:

    def __init__(self):
        self.__watchlist = []

    def add_movie(self, movie):
        if type(movie) == Movie:
            if movie not in self.__watchlist:
                self.__watchlist.append(movie)

    def remove_movie(self, movie):
        if type(movie) == Movie:
            if movie in self.__watchlist:
                self.__watchlist.remove(movie)

    def select_movie_to_watch(self, index):
        if index < len(self.__watchlist):
            return self.__watchlist[index]
        return None

    def size(self):
        return len(self.__watchlist)

    def first_movie_in_watchlist(self):
        if len(self.__watchlist) > 0:
            return self.__watchlist[0]

        return None

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n < len(self.__watchlist):
            movie = self.__watchlist[self.n]
            self.n += 1
            return movie
        else:
            raise StopIteration

    # Extra methods: add a random movie to watchlist
    def add_random(self, movie_list, seed=None):
        random_movie = None

        if seed is None:
            loop = True
            while loop:
                random_movie = random.choice(movie_list)
                if random_movie not in self.__watchlist:
                    self.__watchlist.append(random_movie)
                    break
        else:
            ran = Random(seed)
            loop = True
            while loop:
                random_movie = movie_list[ran.randint(0, len(movie_list) - 1)]
                if random_movie not in self.__watchlist:
                    self.__watchlist.append(random_movie)
                    break

        return random_movie








