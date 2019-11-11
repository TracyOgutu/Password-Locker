#!/usr/bin/env python3.6
import random
from user import User
from credential import Credential


def create_user(usern, userpass):
    new_user = User(usern, userpass)

    return new_user


def save_users(user):
    user.save_user()


def del_user(user):
    user.delete_user()


def login(user, passw):
    login = User.login(user, passw)
    if login != False:
        return User.login(user, passw)


def generate_password(name):
    password = Credential.generate_password()
    return password


def find_user(username):
    return User.find_by_username(username)


def checking_existing_users(username):
    return User.user_exist(username)


def display_users():
    return User.display_users()


def create_credential(nameofuser, accname, accpass):
    new_credential = Credential(nameofuser, accname, accpass)

    return new_credential


def save_credentials(credential):
    credential.save_credential()


def del_credential(credential):
    credential.delete_credential()


def find_credential(accountname):
    return Credential.find_by_accountname(accountname)


def checking_existing_credentials(accountname):
    return User.user_exist(accountname)


def display_credential():
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
            save_users(create_user(usern, userpass))

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
            user = input()

            print("Enter the password")
            passw = input()

            if login(user, passw) == None:
                print("\n")
                print("Please try again or create an account")
                print("\n")

            else:

                login(user, passw)
                print("\n")
                print(f'''{user} welcome to your Credentials\n
                            Use these short codes to get around''')

                while True:

                    print('''  Short codes:
                                    ac - add a credential \n
                                    dc - display credentials \n
                                    ex - exit Credentials''')
            # Get short code from the user

                    short_code = input().lower()
                    if short_code == 'ac':

                        print("\n")
                        print("New Credential")
                        print("-"*10)

                        print("Your Username")
                        username = input()

                        print("Name of the account ...")
                        accname = input()

                        print('''Choose password option\n ap:Automatically generated password \n mp.Make your own password''')
                        
                        option = input()
                        

                        if option == 'mp':
                            print("Password of the credential ...")
                            acc_pass = input().lower()
                        else:
                            x = []
                            r = range(10,500)
                            for n in r:
                                x.append(str(n))
                            acc_pass = (username+accname+random.choice(x))
                            print(f"Your generated password is: {acc_pass}")
                        # else:
                        #     print("Please select the correct short code")


                        # Create and save new user
                        save_credentials(create_credential(
                            username, accname, acc_pass))

                        print("\n")
                        print(
                            f"Credentials for {accname} have been created and saved")
                        print("\n")

                    elif short_code == 'dc':
                        if display_credential():
                            print("Here is a list of all your credentials")
                            print('\n')

                            for credential in display_credential():
                                print(
                                    f"Username: {credential.user_name}  \nAccount: {credential.accountname}\nPassword: {credential.accountpassword}\n")

                            print('\n')
                        else:
                            print('\n')
                            print("You dont seem to have any credentials saved yet")
                            print('\n')

                    elif short_code == 'ex':
                        print("You have exited your credentials.")

                        break

                    else:
                        print("Try again. Please enter correct short codes")
                        
        elif short_code == 'ex':
            print("Thank you. See you next time.")

            break
        else:
            print("Try again. Please enter correct short codes")




if __name__ == '__main__':
    main()
