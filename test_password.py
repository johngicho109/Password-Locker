import unittest
from password import User, Credentials

class TestUser(unittest.TestCase,User):
    '''
    Test class that defines test cases for the user class behaviours.
    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = User("Joe", "1234")

    def tearDown(self):
        """
        tearDown method that does clean up after each test case has run.
        """
        User.user_logins = []

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_user.user_name,"Joe")
        self.assertEqual(self.new_user.password,"1234")

    def test_save_user(self):
        '''
        test_save_user test case to test if the user object is saved into the user logins list.
        '''
        self.new_user.save_user()
        self.assertEqual(len(User.user_logins),1)


class TestCredential(unittest.TestCase,Credentials):
    '''
    Test class that defines test cases for the credential class behaviours.
    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_credentials = Credentials("facebook","Joe","Tech","1234")

    def tearDown(self):
        """
        tearDown method that does clean up after each test case has run.
        """
        Credentials.account_credentials = []

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_credentials.account,"facebook")
        self.assertEqual(self.new_credentials.first_name,"Joe")
        self.assertEqual(self.new_credentials.last_name,"Tech")
        self.assertEqual(self.new_credentials.password,"1234")

    def test_save_credentials(self):
        '''
        test_save_credentials test case to test if the credential object is saved into the account credential list.
        '''
        self.new_credentials.save_credentials()
        self.assertEqual(len(Credentials.account_credentials),1)

if __name__ == '__main__':
    unittest.main()