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

if __name__ == '__main__':
    unittest.main()