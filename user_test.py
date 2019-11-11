import unittest
from user import User

class TestUser(unittest.TestCase):

    def setUp(self):

        self.new_user= User("Yani","315674")

    def test_init(self):

        self.assertEqual(self.new_user.username,"Yani")
        self.assertEqual(self.new_user.password,"315674")

    def test_save_user(self):
        self.new_user.save_user()
        self.assertEqual(len(User.user_list),1)
    def tearDown(self):
        User.user_list=[]

    def test_save_multiple_user(self):
        self.new_user.save_user()
        test_user=User("Yoni","345678")
        test_user.save_user()
        self.assertEqual(len(User.user_list),2)

    def test_delete_user(self):
        self.new_user.save_user()
        test_user=User("Yoni","345678")
        test_user.save_user()

        self.new_user.delete_user()
        self.assertEqual(len(User.user_list),1)

    def test_find_user_by_username(self):
        self.new_user.save_user()
        test_user=User("Yoni","345678")
        test_user.save_user()

        found_user= User.find_by_username("Yoni")
        self.assertEqual(found_user.username,test_user.username)

    def test_user_exists(self):

        self.new_user.save_user()
        test_user= User("Yoni","345678")
        test_user.save_user()

        user_exists=User.user_exist("Yoni")

        self.assertTrue(user_exists)
    
    def test_display_all_users(self):

        self.assertEqual(User.display_users(),User.user_list)





if __name__ == '__main__':
    unittest.main()
