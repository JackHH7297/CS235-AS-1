from datafilereaders.movie_file_csv_reader import MovieFileCSVReader
from domainmodel.movie import Movie
from domainmodel.actor import Actor
from domainmodel.genre import Genre
from domainmodel.director import Director


def test_completed_attributes():
    filename = 'datafiles/Data1000Movies.csv'
    movie_file_reader = MovieFileCSVReader(filename)
    movie_file_reader.read_csv_file()

    movie_name = "Guardians of the Galaxy"
    movie = movie_file_reader.movie_object(movie_name)

    # normal attributes
    assert movie.title == "Guardians of the Galaxy"
    assert movie.release_year == 2014
    assert movie.description == "A group of intergalactic criminals are forced to work together " \
                                "to stop a fanatical warrior from taking control of the universe."
    assert movie.director == Director("James Gunn")
    assert movie.actors == [Actor("Chris Pratt"), Actor("Vin Diesel"), Actor("Bradley Cooper"), Actor("Zoe Saldana")]
    assert movie.genres == [Genre("Action"), Genre("Adventure"), Genre("Sci-Fi")]
    assert movie.runtime_minutes == 121

    # extra attributes
    assert movie.rank == 1
    assert movie.rating == 8.1
    assert movie.revenue == 333.13
    assert movie.votes == 757074
    assert movie.metascore == 76


def test_incomplete_attributes():
    filename = 'datafiles/Data1000Movies.csv'
    movie_file_reader = MovieFileCSVReader(filename)
    movie_file_reader.read_csv_file()

    movie_name = "Hounds of Love"
    movie = movie_file_reader.movie_object(movie_name)

    # normal attributes
    assert movie.title == "Hounds of Love"
    assert movie.release_year == 2016
    assert movie.description == "A cold-blooded predatory couple while cruising the streets in search of their " \
                                "next victim, will stumble upon a 17-year-old high school girl, who will be sedated, " \
                                "abducted and chained in the strangers' guest room."
    assert movie.director == Director("Ben Young")
    assert movie.actors == [Actor("Emma Booth"),Actor("Ashleigh Cummings"), Actor("Stephen Curry"),
                            Actor("Susie Porter")]
    assert movie.genres == [Genre("Crime"), Genre("Drama"), Genre("Horror")]
    assert movie.runtime_minutes == 108

    # extra attributes
    assert movie.rank == 23
    assert movie.rating == 6.7
    assert movie.revenue is None
    assert movie.votes == 1115
    assert movie.metascore == 72


def test_filter_by_a_genre():
    filename = 'datafiles/Data1000Movies.csv'
    movie_file_reader = MovieFileCSVReader(filename)
    movie_file_reader.read_csv_file()

    genre = Genre("War")
    movie_file_reader.filter_by_genre(genre)
    assert len(movie_file_reader.movies_filtered_by_genre) == 13
    assert movie_file_reader.movies_filtered_by_genre == [Movie("Inglourious Basterds", 2009), Movie("300", 2006),
                                                        Movie("Mine", 2016),
                                                        Movie("Billy Lynn's Long Halftime Walk", 2016),
                                                        Movie("Pan's Labyrinth", 2006), Movie("Fury", 2014),
                                                        Movie("Macbeth", 2015),
                                                        Movie("The Boy in the Striped Pyjamas", 2008),
                                                        Movie("Frantz", 2016), Movie("Incendies", 2010),
                                                        Movie("Eye in the Sky", 2015), Movie("Suite Française", 2014),
                                                        Movie("Rambo", 2008)]


def test_filter_by_list_of_genres():
    filename = 'datafiles/Data1000Movies.csv'
    movie_file_reader = MovieFileCSVReader(filename)
    movie_file_reader.read_csv_file()

    genre = [Genre("Action"), Genre("Crime"), Genre("Mystery")]
    movie_file_reader.filter_by_genre(genre)
    assert len(movie_file_reader.movies_filtered_by_genre) == 3
    assert movie_file_reader.movies_filtered_by_genre == [Movie("Salt", 2010), Movie("Jack Reacher", 2012),
                                                        Movie("Escape Plan", 2013)]


def test_filter_by_genres_illeage_inputs():
    filename = 'datafiles/Data1000Movies.csv'
    movie_file_reader = MovieFileCSVReader(filename)
    movie_file_reader.read_csv_file()

    genre = Genre("Good")
    movie_file_reader.filter_by_genre(genre)
    assert movie_file_reader.movies_filtered_by_genre == []

    genre = [Genre("Happy")]
    movie_file_reader.filter_by_genre(genre)
    assert movie_file_reader.movies_filtered_by_genre == []

    genre = 123456
    movie_file_reader.filter_by_genre(genre)
    assert movie_file_reader.movies_filtered_by_genre == []


def test_filter_by_director_normal():
    filename = 'datafiles/Data1000Movies.csv'
    movie_file_reader = MovieFileCSVReader(filename)
    movie_file_reader.read_csv_file()

    director = Director("James Gunn")
    movie_file_reader.filter_by_director(director)
    assert movie_file_reader.movies_filtered_by_director == [Movie("Guardians of the Galaxy", 2014),
                                                           Movie("Slither", 2006),
                                                           Movie("Super", 2010)]


def test_filter_by_director_illeagal_inputs():
    filename = 'datafiles/Data1000Movies.csv'
    movie_file_reader = MovieFileCSVReader(filename)
    movie_file_reader.read_csv_file()

    director = Director("Nier Automata")
    movie_file_reader.filter_by_director(director)
    assert movie_file_reader.movies_filtered_by_director == []

    director_1 = "James Gunn"
    movie_file_reader.filter_by_director(director_1)
    assert movie_file_reader.movies_filtered_by_director == []

    director_2 = 12345
    movie_file_reader.filter_by_director(director_2)
    assert movie_file_reader.movies_filtered_by_director == []

