class User():
    """
    A class that generates Users Login details.
    """
    user_logins = []
    def __init__(self, user_name, password):
        """
        __init__ method that helps us define properties for our objects.
        Args:
            user_name: New user user name.
            password : New user password.
        """
        self.user_name = user_name
        self.password = password

    def save_user(self):
        '''
        save_user method saves user objects into user_login list.
        '''
        self.user_logins.append(self)

class Credentials():
    """
    A class that generates credential details.
    """
    account_credentials = []

    def __init__(self,account,first_name,last_name,password):
        """
        __init__ method that helps us define properties for our objects.
        Args:
        account: User account.
        first_name: User account first_name.
        last_name: User account first_name.
        password : user account password.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.account = account
        self.password = password

    def save_credentials(self):
        """
        save_credential method saves credential objects into account credential  list.
        """
        self.account_credentials.append(self)
