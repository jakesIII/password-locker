import unittest
from user import User
from credentials import Credentials

class TestUser(unittest.TestCase):
    '''defines test cases for user methods'''

    def setUp(self):
        '''set up a method to run before each case '''

        self.new_user = User("Jakes", "deepinthot")
        self.generate = Credentials ("twitter", "lordSpiral", "sitUp!")


    def test_init(self):
        '''Testing to see if the object is properly initialized'''

        self.assertEqual(self.new_user.username, "Jakes")
        self.assertEqual(self.new_user.password, "deepinthot")

        self.assertEqual(self.generate.app_title, "twitter")
        self.assertEqual(self.generate.acc_name, "lordSpiral")
        self.assertEqual(self.generate.acc_password, "sitUp!")

    def test_saved_acc(self):
        '''Test case saving username and passwords'''

        self.assertEqual(len(User.account_list), 0)

    def test_user_auth(self):
        '''Test is user login'''

        self.new_user.save_acc()
        test_user = User ("Derrik", "derrick452")
        test_user.save_acc()

        user_exist = User.user_auth("Jakes", "deepinthot")

        self.assertTrue(user_exist)

    def test_save_data(self):
        '''Tests if data is being saved'''

        self.assertEqual(len(Credentials.generated), 2)

    def test_delete_data(self):
        '''Tests if data is removed from list'''

        self.generate.save_data()
        test_data = Credentials ("insta", "obj", "GangSigns")
        test_data.save_data()

        self.generate.delete_data()
        self.assertEqual(len(Credentials.generated), 1)

    def test_random_password(self):

        generated_password = Credentials.random_password(12)
        test_data = Credentials ("gmail", "obj", generated_password)
        test_data.save_data()

        self.assertEqual(len(test_data.acc_password), 12)

























    #     def test_saved_accounts(self):
    #     '''Test case for multiple saved accounts'''
    #
    #     self.new_user.save_acc ()
    #     test_user = User ("Derrik", "derrick452")
    #     test_user.save_acc()
    #     self.assertEqual(len(User.account_list), 5)
    #
    # def test_delete_acc(self):
    #     '''test case to determine if we can remove account from list'''
    #
    #     self.new_user.save_acc()
    #     test_user = User ("Derrik", "derrick452")
    #     test_user.save_acc()
    #
    #     self.new_user.delete_acc()
    #     self.assertEqual(len(User.account_list), 1)
    #
    # def test_find_by_username(self):
    #     '''test to find user by username'''
    #
    #     self.new_user.save_acc()
    #     test_user = User ("Derrik", "derrick452")
    #     test_user.save_acc()
    #
    #     located_user = User.find_by_username("Derrik")
    #
    #     self.assertEqual(located_user.username, test_user.username)
    #
    # def test_display_account(self):
    #     '''test to display user'''
    #
    #     self.assertEqual(User.display_account(), User.account_list)

if __name__ == '__main__':
    unittest.main()
