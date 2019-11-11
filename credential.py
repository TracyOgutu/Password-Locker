from random import choice
import string
class Credential:

    def __init__(self,username,accountname,accountpassword):

        self.username=username
        self.accountname=accountname
        self.accountpassword=accountpassword

    credential_list=[]

    def save_credential(self):
        Credential.credential_list.append(self)

    def delete_credential(self):
        Credential.credential_list.remove(self)

    @classmethod
    def find_by_accountname(cls,accountname):

        for credential in cls.credential_list:
            if credential.accountname==accountname:
                return credential

    @classmethod
    def credential_exist(cls,accountname):

        for credential in cls.credential_list:
            if credential.accountname==accountname:
                return True
          
        return False

    @classmethod  #when to use classmethod
    def display_credentials(cls):

        return cls.credential_list

    @classmethod
    def generate_password(cls):
        # Length of the generated password
        size = 8

        # Generate random alphanumeric 
        alphanum = string.ascii_uppercase + string.digits + string.ascii_lowercase

        # Create password
        password = ''.join( choice(alphanum) for num in range(size) )
        
        return password
