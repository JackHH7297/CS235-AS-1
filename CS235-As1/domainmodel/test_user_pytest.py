from domainmodel.movie import Movie
from domainmodel.review import Review
from domainmodel.user import User


def test_user_password_normal():
    user = User("    Jack Huang     ", "gOod one")

    assert user.user_name == "jack huang"
    assert user.password == "gOod one"


def test_user_password_non_string():
    user = User(1234124, 123124)

    assert user.user_name is None
    assert user.password is None


def test_user_password_string_int():
    user = User("Jack Huang", "123124")

    assert user.user_name == "jack huang"
    assert user.password == "123124"


def test_empty_watched_movies_and_reviews():
    user = User("Jack Huang", "123124")

    assert user.watched_movies == []
    assert user.reviews == []


def test_add_movies_and_length():
    user = User("Jack Huang", "123124")
    movie1 = Movie("Your Name", 2000)
    movie2 = Movie("Spirited Away", 1995)
    movie3 = Movie("Avengers 4", 1899)
    movie1.runtime_minutes = 100
    movie2.runtime_minutes = 150
    movie3.runtime_minutes = 300

    assert user.watched_movies == []
    user.watch_movie(movie1)
    user.watch_movie(movie2)
    user.watch_movie(movie3)
    assert user.watched_movies == [Movie("Your Name", 2000), Movie("Spirited Away", 1995), Movie("Avengers 4", None)]
    assert user.time_spent_watching_movies_minutes == 550


def test_add_review():
    user = User("Jack Huang", "123124")
    movie1 = Movie("Your Name", 2000)
    movie2 = Movie("Spirited Away", 1995)
    movie3 = Movie("Avengers 4", 1899)

    review1 = Review(movie1, "Good 1", 1)
    review2 = Review(movie2, "Good 2", 2)
    review3 = Review(movie3, "Good 3", 3)

    assert user.reviews == []
    user.add_review(review1)
    user.add_review(review2)
    user.add_review(review3)
    assert user.reviews == [Review(movie1, "Good 1", 1), Review(movie2, "Good 2", 2), Review(movie3, "Good 3", 3)]








def test_eq_same_name():
    user1 = User("qwer", 12345)
    user2 = User("qwer", "qwer")

    eq = user1 == user2
    assert eq == True


def test_eq_same_name_caps_space():
    user1 = User(" QweR      ", 12345)
    user2 = User("     qWEr ", "qwer")

    eq = user1 == user2
    assert eq == True


def test_eq_diff_name():
    user1 = User(" Q weR      ", 12345)
    user2 = User("     qWEr ", "qwer")

    eq = user1 == user2
    assert eq == False


def test_lt_same_name():
    user1 = User(" QweR      ", "aaaaa")
    user2 = User("     qWEr ", "A")

    lt = user1 < user2
    assert lt == False


def test_lt_diff_name():
    user1 = User("Hi", 12345)
    user2 = User("HI", "qwer")

    lt = user1 < user2
    assert lt == False


def test_lt_none_name():
    user1 = User(None, 12345)
    user2 = User("HI", "qwer")

    lt = user1 < user2
    assert lt == True


def test_hash_():
    user1 = User("None", "qwer")
    user2 = User("HI", "qwer")
    user3 = User("Jack", "qwer")
    user4 = User("  jack      ", "qwer")

    seta = {user1, user2, user3, user4}
    assert seta == {User("None", "qwer"), User("HI", "qwer"), User("Jack", "qwer"), User("  jack      ", "qwer")}



