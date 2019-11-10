class User:
    ''' class that generates a new instance of users '''

    account_list = []


    def __init__(self, username, password):

        '''define object properties '''

        self.username = username
        self.password = password

    def save_acc(self):

        User.account_list.append(self)

    def delete_acc(self):
        User.account_list.remove(self)
