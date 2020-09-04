from domainmodel.genre import Genre
from domainmodel.actor import Actor
from domainmodel.director import Director


class Movie:

    def __init__(self, title = None, year = None):
        if title == None:
            self.__title = None
        elif title != None and type(title) == str and title != "":
            self.__title = title.strip()
        else:
            self.__title = None

        if year == None:
            self.__release_year = None
        elif year != None and type(year) == int and year >= 1900:
            self.__release_year = year
        else:
            self.__release_year = None

        self.__director = None
        self.__description = ""
        self.__runtime_minutes = 0
        self.__actor_list = []
        self.__genres_list = []

        # Extension
        self.__rank = None
        self.__rating = None
        self.__revenue = None
        self.__metascore = None
        self.__votes = None

    @property
    def rank(self):
        return self.__rank

    @rank.setter
    def rank(self, rank):
        try:
            rank = int(rank)
            if type(rank) == int:
                if rank > 0:
                    self.__rank = rank
        except ValueError:
            pass

    @property
    def rating(self):
        return self.__rating

    @rating.setter
    def rating(self, rating):
        try:
            rating = float(rating)
            if 1 <= rating <= 10:
                self.__rating = rating
        except ValueError:
            pass

    @property
    def revenue(self):
        return self.__revenue

    @revenue.setter
    def revenue(self, revenue):
        try:
            revenue = float(revenue.strip())
            self.__revenue = revenue
        except ValueError:
            pass

    @property
    def metascore(self):
        return self.__metascore

    @metascore.setter
    def metascore(self, score):
        try:
            score = int(score.strip())
            if 0 <= score <= 100:
                self.__metascore = score
        except ValueError:
            pass

    @property
    def votes(self):
        return self.__votes

    @votes.setter
    def votes(self, vote):
        try:
            vote = int(vote)
            if vote >= 0:
                self.__votes = vote
        except ValueError:
            pass

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, movie_name):
        if isinstance(movie_name, str) and movie_name != "":
            self.__title = movie_name.strip()

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, descript):
        if isinstance(descript, str) and descript != "":
            self.__description = descript.strip()

    @property
    def actors(self):
        return self.__actor_list

    @actors.setter
    def actors(self, list_of_actors):
        if type(list_of_actors) == list:
            for i in list_of_actors:
                if type(i) != Actor:
                    return
            self.__actor_list = list_of_actors
        else:
            if type(list_of_actors) == Actor:
                self.__actor_list.append(list_of_actors)

    @property
    def genres(self):
        return self.__genres_list

    @genres.setter
    def genres(self, list_of_genres):
        if type(list_of_genres) == list:
            for i in list_of_genres:
                if type(i) != Genre:
                    return
            self.__genres_list = list_of_genres
        else:
            if type(list_of_genres) == Genre:
                self.__genres_list.append(list_of_genres)

    @property
    def director(self):
        return self.__director

    @director.setter
    def director(self, a_director):
        if type(a_director) == Director:
            self.__director = a_director

    @property
    def runtime_minutes(self):
        return self.__runtime_minutes

    @runtime_minutes.setter
    def runtime_minutes(self, value):
        if type(value) == int:
            if value <= 0:
                raise ValueError
            else:
                self.__runtime_minutes = value

    def __repr__(self):
        return "<Movie {}, {}>".format(self.__title, self.__release_year)

    def __eq__(self, other):
        if self.__title == other.__title:
            if self.__release_year == other.__release_year:
                return True
        return False

    def __lt__(self, other):
        if self.__title == None or other.__title == None:
            if other.__title != None:
                return True
            else:
                if self.__release_year == None and other.__release_year == None:
                    return False
                elif self.__release_year != None:
                    if other.__release_year != None:
                        if self.__release_year < other.__release_year:
                            return True
                        else:
                            return False
                    else:
                        return False

        elif self.__title < other.__title:
            return True

        elif self.__title == other.__title:
            if self.__release_year == None and other.__release_year == None:
                return False
            elif self.__release_year != None:
                if other.__release_year != None:
                    if self.__release_year < other.__release_year:
                        return True
                else:
                    return False
            elif self.__release_year == None:
                if other.__release_year != None:
                    return True

        return False

    def __hash__(self):
        unique_name = self.__title + str(self.__release_year)
        return hash(unique_name)

    def add_actor(self, add_actor):
        if type(add_actor) == Actor:
            self.__actor_list.append(add_actor)

    def remove_actor(self, remove_actor):
        if remove_actor in self.__actor_list:
            self.__actor_list.remove(remove_actor)

    def add_genre(self, add_genre):
        if type(add_genre) == Genre:
            self.__genres_list.append(add_genre)

    def remove_genre(self, remove_genre):
        if remove_genre in self.__genres_list:
            self.__genres_list.remove(remove_genre)

    @property
    def release_year(self):
        return self.__release_year


