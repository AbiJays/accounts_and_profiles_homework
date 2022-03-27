import unittest
from src.account import *
from src.profile import *

class TestAccount(unittest.TestCase):

    def setUp(self):

        # Creating some objects to use in the tests
        self.profile_1 = Profile("harrisonF", "myP@assword")
        self.profile_2 = Profile("markH", "anotherP@ssword")

        self.account_1 = Account("Jane", "Smith", "janes@email.com")


    # Test an Account can add a Profile
    @unittest.skip("delete this line to run the test")
    def test_add_profile(self):
        self.account_1.add_profile(self, added_profile)
        self.assertEqual(3, len(self.account_1.profile_list))

    # Test an Account can remove a given Profile
    @unittest.skip("delete this line to run the test")
    def test_remove_profile(self):
        self.account_1.remove_profile(self, removed_profile)
        self.assertEqual(1, len(self.account_1.profile_list))


    # Test an Account can return a list of Profiles
    @unittest.skip("delete this line to run the test")
    def test_return_profiles_list(self):
        self.assertEqual(2, len(self.account_1.profile_list))