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

def display_users():
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
        usern = input()

        print(f"Hello {usern}. what would you like to do?")
        print('\n')

        while True:
                    print('''Use these short codes :
                     cp - create a password locker account \n
                     du - display the users available\n
                     lg - Log in to your password locker account\n
                     ex - exit the password locker\n ''')

                    short_code = input().lower()


                    if short_code == 'cp':
                        '''
                        Creating a Password Locker account
                        '''

                        print("\n")
                        print("New Password Locker Account")
                        print("-"*10)

                        print("User name ...")
                        usern = input()

                        print("Password ...")
                        userpass = input()

                        # Create and save new user
                        save_users( create_user( usern, userpass) )

                        print("\n")
                        print(f"{usern} welcome to Password Locker")
                        print("\n")

                    elif short_code == 'du':
                        '''
                        Display the names of the current users 
                        '''

                        if display_users():
                            print("\n")
                            print("Here are the current users of Password Locker")
                            print("-"*10)

                            for user in display_users():
                                print(f"{user.username}")
                                print("-"*10)
                        else:
                            print("\n")
                            print("Password Locker has no current user.\n    Be the first user :)")
                            print("\n")

                    elif short_code == 'lg':
                            '''
                            Logs in the user into their Password Locker account
                            '''
                            print("\n")
                            print("Log into Password Locker Account")
                            print("Enter the user name")
                            user_name = input()

                            print("Enter the password")
                            user_password = input()


                    if user_log_in(user_name,user_password) == None:
                        print("\n")
                        print("Please try again or create an account")
                        print("\n")

                    else:

                        user_log_in(user_name,user_password)
                        print("\n")
                        print(f'''{user_name} welcome to your Credentials\n
                        Use these short codes to get around''')




if __name__ == '__main__':
        main()

