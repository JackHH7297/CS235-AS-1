from domainmodel.movie import Movie
from domainmodel.watchlist import WatchList
from domainmodel.genre import Genre
from domainmodel.director import Director
from datafilereaders.movie_file_csv_reader import MovieFileCSVReader


def test_add_same_movie():
    watchlist = WatchList()
    watchlist.add_movie(Movie("Your Name",  2006))
    watchlist.add_movie(Movie("Your Name",  2006))
    assert watchlist.size() == 1


def test_check_size():
    watchlist = WatchList()
    watchlist.add_movie(Movie("Your Name", 2006))
    watchlist.add_movie(Movie("Avengers 4", 2019))
    assert watchlist.size() == 2


def test_remove_movie_in_list():
    watchlist = WatchList()
    watchlist.add_movie(Movie("Your name", 2006))
    watchlist.remove_movie(Movie("Your name", 2006))
    assert watchlist.size() == 0


def test_remove_movie_not_in_list():
    watchlist = WatchList()
    watchlist.remove_movie(Movie("Your name", 2006))
    assert watchlist.size() == 0


def test_index_watchlist():
    watchlist = WatchList()
    watchlist.add_movie(Movie("Your name", 2006))
    assert watchlist.select_movie_to_watch(0) == Movie("Your name", 2006)


def test_index_out_of_bound_watchlist():
    watchlist = WatchList()
    watchlist.add_movie(Movie("Your name", 2006))
    assert watchlist.select_movie_to_watch(1) is None


def test_iter():
    watchlist = WatchList()
    watchlist.add_movie(Movie("Your name", 2006))
    watchlist.add_movie(Movie("Your", 2006))
    watchlist.add_movie(Movie("Your n", 2006))

    i = iter(watchlist)
    assert (next(i)) == Movie("Your name", 2006)
    assert (next(i)) == Movie("Your", 2006)
    assert (next(i)) == Movie("Your n", 2006)


def test_five_random_movie_from_all_movies():
    seed = 116
    watchlist = WatchList()

    filename = 'datafiles/Data1000Movies.csv'
    movie_file_reader = MovieFileCSVReader(filename)
    movie_file_reader.read_csv_file()
    movie_list = movie_file_reader.dataset_of_movies

    random_movie_1 = watchlist.add_random(movie_list, seed)
    assert random_movie_1 == movie_list[841]

    random_movie_2 = watchlist.add_random(movie_list, seed)
    assert random_movie_2 == movie_list[763]

    random_movie_3 = watchlist.add_random(movie_list, seed)
    assert random_movie_3 == movie_list[614]

    random_movie_4 = watchlist.add_random(movie_list, seed)
    assert random_movie_4 == movie_list[559]

    random_movie_5 = watchlist.add_random(movie_list, seed)
    assert random_movie_5 == movie_list[739]

    assert watchlist.size() == 5


def test_movie_list_filtered_by_genres():
    seed = 116
    watchlist = WatchList()

    filename = 'datafiles/Data1000Movies.csv'
    movie_file_reader = MovieFileCSVReader(filename)
    movie_file_reader.read_csv_file()

    genre = Genre("War")
    movie_file_reader.filter_by_genre(genre)
    movie_list = movie_file_reader.movies_filtered_by_genre

    random_movie_1 = watchlist.add_random(movie_list, seed)
    assert random_movie_1 == movie_list[11]

    random_movie_2 = watchlist.add_random(movie_list, seed)
    assert random_movie_2 == movie_list[9]

    random_movie_3 = watchlist.add_random(movie_list, seed)
    assert random_movie_3 == movie_list[8]

    assert watchlist.size() == 3


def test_movie_list_filtered_by_director_duplicates():
    seed = 116
    watchlist = WatchList()

    filename = 'datafiles/Data1000Movies.csv'
    movie_file_reader = MovieFileCSVReader(filename)
    movie_file_reader.read_csv_file()

    director = Director("James Gunn")
    movie_file_reader.filter_by_director(director)
    movie_list = movie_file_reader.movies_filtered_by_director

    random_movie_1 = watchlist.add_random(movie_list, seed)
    assert random_movie_1 == movie_list[2]

    random_movie_2 = watchlist.add_random(movie_list, seed)
    assert random_movie_2 == movie_list[1]

    random_movie_2 = watchlist.add_random(movie_list, seed)
    assert random_movie_2 == movie_list[0]

    assert watchlist.size() == 3

