import unittest
from src.profile import *
from src.movie import *

class TestProfile(unittest.TestCase):

    def setUp(self):

        # Creating some objects to use in the tests
        self.movie_1 = Movie("The Fugitive", "Andrew Daivs", 9)
        self.movie_2 = Movie("Hunger Games", "Gary Ross", 7)

        self.profile_1 = Profile("harrisonF", "myP@assword")

        

    # Test a Profile can add a favourite Movie
    def test_add_movie_to_favourites(self): # always only reference self for tests 
        profile.add_movie(self, new_fave)
        self.assertEqual(3, len(self.profile.favourites))


    # Test a Profile can remove a given Movie from favourites
    @unittest.skip("delete this line to run the test")
    def test_remove_movie_from_favourites(self):
        profile.remove_movie(self, old_fave
        self.assertEqual(2, len(self.profile.favourites))


    # Test a Profile can return a list of Favourites
    @unittest.skip("delete this line to run the test")
    def test_return_favourites(self):
        profile.return_favourites(self)
        self.assertEqual(self.profile_1.favourites)

   
# TO DO
# need to change profile to reference profile_1 object in test
# make list of self.profile_1's favourites›
# make new_fave movie object to add.