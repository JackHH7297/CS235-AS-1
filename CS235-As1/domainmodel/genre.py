class Genre:

    def __init__(self, genre):
        if genre != "":
            self.genre_name = genre
        else:
            self.genre_name = None

    def __repr__(self):
        return "<Genre {}>".format(self.genre_name)

    def __eq__(self, other):
        return self.genre_name == other.genre_name

    def __lt__(self, other):
        return self.genre_name < other.genre_name

    def __hash__(self):
        return hash(self.genre_name)

