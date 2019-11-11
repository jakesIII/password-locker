import random
import pyperclip
import string


class Credentials:
    '''class to instanciate new account credentials'''

    generated = []

    def __init__(self, app, password):
        self.app = app
        self.acc_name = acc_name
        self.acc_password = acc_password

    def save_data(self):
        '''Method that saves our accounts'''
        Credentials.generated.append(self)

    def delete_data(self):
        '''Method to delete an account of our list'''

        Credentials.generated.remove(self)

    def random_password(self):
        '''method to generate a random password'''

        characters = string.ascii_lowercase + string.digits
        gen_password = ''.join(random.choice(char) for i in range (0,9))

        return random_password
