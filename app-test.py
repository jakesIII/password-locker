import unittest
from user import User

class TestUser(unittest.TestCase):
    '''defines test cases for user methods'''

    def setUp(self):
        '''set up a method to run before each case '''

        self.new_user = User("Jakes", "deepinthot")

    def test_init(self):
        '''Testing to see if the object is properly initialized'''

        self.assertEqual(self.new_user.username, "Jakes")
        self.assertEqual(self.new_user.password, "deepinthot")

    def test_saved_acc(self):
        '''Test case saving username and passwords'''

        self.assertEqual(len(User.account_list), 0)

    def test_saved_accounts(self):

        self.assertEqual(len(User.account_list), 2)

if __name__ == '__main__':
    unittest.main()
