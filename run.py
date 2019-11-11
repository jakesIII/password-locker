#!/usr/bin/env python3.6

from credentials import Credentials
from user import User
import random

def create_user (username, password):
    '''function to create a new user '''

    new_acc = User (username, password)

    return new_acc

def users_data(app_title, acc_name, acc_password):
    '''Function to create a new data entry'''

    new_data = Credentials (app_title, acc_name, acc_password)

    return new_data

def authenticate_user(username, password):
    '''Function to authenticate user'''

    return User.user_auth(username, password)

def save_created_user(user):
    '''Function to store user information'''

    user.save_acc()

def save_user_data(credentials):
    '''Function to store user data'''

    credentials.save_data()

def display_data():
    '''Function to display saved data'''

    return credentials.display_account()

def delete_data():
    '''Function to remove stored data'''

    credentials.delete_data()

def pass_generate(length):
    '''Function to create a random password'''

    return Credentials.random_password(length)

def main():
    print("This is password locker! To sign up, key 'su', to log in, key 'li' ...")
    answer = input ('>>> ')

    if answer = "li":

        print("Enter a Username: ")
        username = input('Enter username: ')

        print("Enter a password: ")
        password = input ('Enter password: ')

    log_in = authenticate_user(username, password) if answer == 'li' else False

    while log_in:
        print("Use the following short codes to navigate \n ad - to save an existing account data \n cd - to create new account data \n vd - to view list of inputed data \n dd - to delete account data from list")
        short_code = input(">>>")

        if short_code == "ad":
            print ("Enter existing account data...")

            print ("Enter the name of the account")
            app_title = input(">>>")

            print ("Enter the username to the account")
            acc_name = input (">>>")

            print ("Enter the account's password")
            acc_password = input (">>>")

            save_data(users_data(app_title, acc_name, acc_password))

            print (f"Data for {app_title} has been saved.")

        elif short_code == "cd":
            print ("Create new account data...")

            print ("Enter the name of the account")
            app_title = input(">>>")

            print ("Enter the username to the account")
            acc_name = input (">>>")

            print ("For the password; \n key in 'y' if you want a generated password \n 'n' if you want to input a custom one ")
            answer_password = input(">>>")

            if answer_password == "y":
                print("Input password preffered length...")
                pass_length= int(input(">>>"))
                gener_password = pass_generate(pass_length)
                print(f"{app_title}'s password is {gener_password}")

            elif answer_password == "n":
                print("Input your own password")
                acc_password = input (">>>")

            else:
                print ("Your choice is in valid, try again")

            save_data(users_data(app_title, acc_name, acc_password))

            print (f"Data for {app_title} has been saved.")
            print('\n')

        elif short_code == "vd":
                if display_data():
                    print("Here is a list of all your stored account data")
                    print('\n')

                    for data in display_data():
                        print (f"Application Title >>> {data.app_title}")
                        print (f"Application Username >>> {data.acc_name}")
                        print (f"Application Password >>> {data.acc_password}")

                else:
                    print("You don't seem to have any stored account data")
                    print('\n')

        elif short_code == "dd": 







if __name__ == '__main__':
    main()
