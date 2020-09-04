from datetime import datetime

from domainmodel.movie import Movie


class Review:

    def __init__(self, movie, review_text, rating):
        if type(movie) == Movie:
            self.__movie = movie
        else:
            self.__movie = None

        if type(review_text) == str:
            self.__review_text = review_text
        else:
            self.__review_text = ""

        if 0 < rating < 11:
            self.__rating = rating
        else:
            self.__rating = None

        self.__timestamp = datetime.today()

    def __repr__(self):
        return "{} \nReview: {}\nRating: {}\nDate: {}".\
            format(self.__movie, self.__review_text, self.__rating, self.__timestamp)

    def __eq__(self, other):
        if self.__movie == other.__movie:
            if self.__review_text == other.__review_text:
                if self.__rating == other.__rating:
                    if self.__timestamp == other.__timestamp:
                        return True
        return False

    @property
    def movie(self):
        return self.__movie

    @property
    def review_text(self):
        return self.__review_text

    @property
    def rating(self):
        return self.__rating

    @property
    def timestamp(self):
        return self.__timestamp


