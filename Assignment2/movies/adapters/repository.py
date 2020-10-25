import abc
from typing import List

from movies.domain.model import Director, Actor, Genre, Movie, User, Review

repo_instance = None

class RepositoryException(Exception):
    def __init__(self, message=None):
        pass


class AbstractRepository(abc.ABC):

    @abc.abstractmethod
    def add_user(self, user: User):
        raise NotImplementedError

    @abc.abstractmethod
    def get_user(self, username) -> User:
        raise NotImplementedError

    @abc.abstractmethod
    def add_movie(self, movie: Movie):
        raise NotImplementedError

    @abc.abstractmethod
    def get_movie(self, rank: int) -> Movie:
        raise NotImplementedError

    @abc.abstractmethod
    def get_movie_rank_by_name(self, name: str):
        raise NotImplementedError

    @abc.abstractmethod
    def get_number_of_movies(self):
        raise NotImplementedError

    @abc.abstractmethod
    def get_first_movie(self) -> Movie:
        raise NotImplementedError

    @abc.abstractmethod
    def get_last_movie(self) -> Movie:
        raise NotImplementedError

    @abc.abstractmethod
    def get_movies_by_rank(self, rank_list):
        raise NotImplementedError

    @abc.abstractmethod
    def get_movie_ranks_for_genre(self, genre_name: str):
        raise NotImplementedError

    @abc.abstractmethod
    def add_genre(self, genre: Genre):
        raise NotImplementedError

    @abc.abstractmethod
    def get_genres(self) -> List[Genre]:
        raise NotImplementedError

    @abc.abstractmethod
    def add_actor(self, actor: Actor):
        raise NotImplementedError

    @abc.abstractmethod
    def get_actors(self) -> List[Actor]:
        raise NotImplementedError

    @abc.abstractmethod
    def add_director(self, director: Director):
        raise NotImplementedError

    @abc.abstractmethod
    def get_directors(self) -> List[Director]:
        raise NotImplementedError

    @abc.abstractmethod
    def add_review(self, review: Review):
        """ Adds a Comment to the repository.

        If the Comment doesn't have bidirectional links with an Article and a User, this method raises a
        RepositoryException and doesn't update the repository.
        """
        if review.user is None or review not in review.user.reviews:
            raise RepositoryException('Review not correctly attached to a User')
        if review.movie is None or review not in review.user.reviews:
            raise RepositoryException('Review not correctly attached to an Movie')

    @abc.abstractmethod
    def get_reviews(self):
        raise NotImplementedError


