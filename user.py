from credential import Credential

class User:
    def __init__(self,username,password):
        self.username=username
        self.password=password

    user_list=[]

    def save_user(self):
        User.user_list.append(self)

    def delete_user(self):
        User.user_list.remove(self)

    @classmethod
    def find_by_username(cls,username):

        for user in cls.user_list:
            if user.username==username:
                return user

    @classmethod
    def user_exist(cls,username):

        for user in cls.user_list:
            if user.username==username:
                return True

        return False

    @classmethod  #when to use classmethod
    def display_users(cls):

        return cls.user_list

    @classmethod
    def login(cls,username,password):
        for user in cls.user_list:
            if user.username==username and user.password==password:
                return Credential.credential_list

        return False




    
    
