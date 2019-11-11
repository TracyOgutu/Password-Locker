import unittest

from credential import Credential

class TestCredential(unittest.TestCase):

    def setUp(self):
        self.new_credential=Credential("Yani","Twitter","mytweet")

    def test_init(self):

        self.assertEqual(self.new_credential.user_name,"Yani")
        self.assertEqual(self.new_credential.accountname,"Twitter")
        self.assertEqual(self.new_credential.accountpassword,"mytweet")

    def test_save_credential(self):
        self.new_credential.save_credential()
        self.assertEqual(len(Credential.credential_list),1)
    def tearDown(self):
        Credential.credential_list=[]

    def test_save_multiple_credential(self):
        self.new_credential.save_credential()
        test_credential=Credential("Yoni","Instagram","myinsta")
        test_credential.save_credential()
        self.assertEqual(len(Credential.credential_list),2)


    def test_delete_credential(self):
        self.new_credential.save_credential()
        test_credential=Credential("Yoni","Instagram","myinsta")
        test_credential.save_credential()
        

        self.new_credential.delete_credential()
        self.assertEqual(len(Credential.credential_list),1)

    
    def test_generate_password(self):
        generated_password=self.new_credential.generate_password()
        self.assertEqual(len(generated_password),8)

    def test_find_credential_by_accountname(self):
         self.new_credential.save_credential()

         test_credential=Credential("Yoni","Instagram","myinsta")
         test_credential.save_credential()
        
         found_credential= Credential.find_by_accountname("Instagram")
         self.assertEqual(found_credential.accountname,test_credential.accountname)

    def test_credential_exists(self):
        self.new_credential.save_credential()

        test_credential=Credential("Yoni","Instagram","myinsta")
        test_credential.save_credential()

        credential_exists=Credential.credential_exist("Instagram")

        self.assertTrue(credential_exists)
    
    def test_display_all_credentials(self):

        self.assertEqual(Credential.display_credentials(),Credential.credential_list)

if __name__ == '__main__':
    unittest.main()

    
