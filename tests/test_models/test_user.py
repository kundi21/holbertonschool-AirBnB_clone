#!/usr/bin/python3
"""Unittest for models/user.py"""
import unittest
from models.user import User


class to_Test_User(unittest.TestCase):
    """Test cases for User class"""

    def test_user_instance(self):
        """Test user instance"""
        user = User()
        self.assertIsInstance(user, User)

    def test_user_first_name_str(self):
        """Test user first_name is str"""
        user = User()
        self.assertIsInstance(user.first_name, str)

    def test_user_last_name_str(self):
        """Test user last_name is str"""
        user = User()
        self.assertIsInstance(user.last_name, str)

    def test_user_email_str(self):
        """Test user email is str"""
        user = User()
        self.assertIsInstance(user.email, str)

    def test_user_password_str(self):
        """Test user password is str"""
        user = User()
        self.assertIsInstance(user.password, str)

    def test_user_to_dict(self):
        """Test user to_dict method"""
        user = User()
        self.assertIsInstance(user.to_dict(), dict)

class to_Test_User_save(unittest.TestCase):
    """Test cases for User save method"""

    def test_user_save(self):
        """Test user save method"""
        user = User()
        user.save()
        self.assertNotEqual(user.created_at, user.updated_at)

    def test_user_save_with_arg(self):
        """Test user save method with arg"""
        with self.assertRaises(TypeError):
            user = User().save(None)

class to_Test_User_to_dict(unittest.TestCase):
    """Test cases for User to_dict method"""

    def test_user_to_dict(self):
        """Test user to_dict method"""
        user = User()
        self.assertIsInstance(user.to_dict(), dict)

    def test_user_to_dict_with_arg(self):
        """Test user to_dict method with arg"""
        with self.assertRaises(TypeError):
            user = User().to_dict(None)
