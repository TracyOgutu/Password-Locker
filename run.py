#!/usr/bin/env python3.6
from user import User
from credential import Credential
#creating a user
def create_user(usern,userpass):
    new_user=User(usern,userpass)

    return new_user

def save_users(user):
    user.save_user()

def del_user(user):
    user.delete_user()

def find_user(username):
    return User.find_by_username(username)

def checking_existing_users(username):
    return User.user_exist(username)

def display_contacts():
    return User.display_users()

def create_credential(nameofuser,accname,accpass):
    new_credential=Credential(nameofuser,accname,accpass)

    return new_credential

def save_credentials(credential):
    credential.save_credential()

def del_credential(credential):
    credential.delete_credential()

def find_credential(accountname):
    return Credential.find_by_accountname(accountname)

def checking_existing_credentials(accountname):
    return User.user_exist(accountname)

def display_credentials():
    return Credential.display_credentials()


def main():
        print("Welcome to password locker. What is your name?")
        user_name = input()

        print(f"Hello {user_name}. what would you like to do?")
        print('\n')

        while True:
                    print('''Use these short codes :
                     cc - create a password locker account \n
                     dc - display users\n
                     fc -find a user\n
                     ex -exit the password locker\n ''')

                    short_code = input().lower()

if __name__ == '__main__':
        main()

