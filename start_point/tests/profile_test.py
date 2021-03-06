import unittest
from src.profile import *
from src.movie import *

class TestProfile(unittest.TestCase):

    def setUp(self):

        # Creating some objects to use in the tests
        self.movie_1 = Movie("The Fugitive", "Andrew Daivs", 9)
        self.movie_2 = Movie("Hunger Games", "Gary Ross", 7)

        self.favourites = [self.movie_1, self.movie_2]

        self.profile_1 = Profile("harrisonF", "myP@assword")

        self.movie = Movie("Star Trek", "JJ Abrhams", 9)

    # Test a Profile can add a favourite Movie
    def test_add_movie_to_favourites(self): # always onlßy reference self for tests 
        self.profile_1.add_movie(self.movie)
        self.assertEqual(1, len(self.profile_1.favourites))


    # Test a Profile can remove a given Movie from favourites
    # @unittest.skip("delete this line to run the test")
    def test_remove_movie_from_favourites(self):
        self.profile_1.add_movie(self.movie_1)
        self.profile_1.add_movie(self.movie_2)
        self.profile_1.remove_movie(self, self.movie)
        self.assertEqual(1, len(self.profile_1.favourites))


    # Test a Profile can return a list of Favourites
#   @unittest.skip("delete this line to run the test")
    def test_return_favourites(self):
        self.profile_1.add_movie(self.movie_1)
        self.profile_1.add_movie(self.movie_2)
        self.assertEqual([self.movie_1, self.movie_2], self.profile_1.favourites)

   
# TO DO
# need to change profile to reference profile_1 object in test
# make list of self.profile_1's favourites›
# make new_fave movie object to add.

# Absolutely

# Don't forget self.profile probably for most tests

# And in the last one, you can check if the return value of your function is the same as the original movie list from the setUp up top