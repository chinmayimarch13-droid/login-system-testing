import unittest
from app import login

class TestLogin(unittest.TestCase):

    def test_valid_login(self):
        self.assertEqual(login("admin", "1234"), "Login Successful")

    def test_invalid_login(self):
        self.assertEqual(login("admin", "0000"), "Invalid Credentials")

    def test_empty_fields(self):
        self.assertEqual(login("", ""), "Fields cannot be empty")

    def test_short_password(self):
        self.assertEqual(login("admin", "12"), "Password too short")

if __name__ == "__main__":
    unittest.main()
