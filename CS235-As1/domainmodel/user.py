from domainmodel.movie import Movie
from domainmodel.review import Review

class User:

    def __init__(self, username, password):
        if type(username) == str:
            self.__user_name = username.strip().lower()
        else:
            self.__user_name = None

        if type(password) == str:
            self.__password = password
        else:
            self.__password = None

        self.__watched_movies = []
        self.__reviews = []
        self.__time_spent_watching_movies_minutes = 0

    def __repr__(self):
        return "<User {}>".format(self.__user_name)

    def __eq__(self, other):
        return self.__user_name == other.__user_name

    def __lt__(self, other):
        if self.__user_name is None:
            if other.__user_name is None:
                return False
            else:
                return True
        else:
            if other.__user_name is None:
                return False
            else:
                return self.__user_name < other.__user_name

    def __hash__(self):
        return hash(self.__user_name)

    def watch_movie(self, movie):
        if type(movie) == Movie:
            self.__watched_movies.append(movie)
            self.__time_spent_watching_movies_minutes += movie.runtime_minutes

    def add_review(self, review):
        if type(review) == Review:
            self.__reviews.append(review)

    @property
    def user_name(self):
        return self.__user_name

    @property
    def password(self):
        return self.__password

    @property
    def watched_movies(self):
        return self.__watched_movies

    @property
    def reviews(self):
        return self.__reviews

    @property
    def time_spent_watching_movies_minutes(self):
        return self.__time_spent_watching_movies_minutes
