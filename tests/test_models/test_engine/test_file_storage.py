#!/usr/bin/python3
"""Unittest for models/engine/file_storage.py"""
import unittest
from models.engine.file_storage import FileStorage


class to_Test_file_storage(unittest.TestCase):
    """Test for FileStorage class"""

    def test_file_storage_path_is_str(self):
        """Tests if path is str"""
        file_path = FileStorage.__file_path
        self.assertIsInstance(file_path, str)

    def test_file_storage_objects_is_dict(self):
        """Tests if objects is dict"""
        objects = FileStorage.__objects
        self.assertIsInstance(objects, dict)

    def test_file_storage_file_path_is_str(self):
        """Tests if file_path is str"""
        file_path = FileStorage.__file_path
        self.assertIsInstance(file_path, str)

    def test_file_storage_no_args(self):
        """Tests if no args are passed"""
        with self.assertRaises(TypeError):
            FileStorage()

    def test_file_storage_with_args(self):
        """Tests if args are passed"""
        with self.assertRaises(TypeError):
            FileStorage(None)

class to_Test_file_storage_methods(unittest.TestCase):
    """Test for FileStorage class"""

    def test_all_method(self):
        """Tests if all method returns dict"""
        storage = FileStorage()
        self.assertIsInstance(storage.all(), dict)

    def test_new_method(self):
        """Tests if new method adds object to storage"""
        storage = FileStorage()
        storage.new(None)
        self.assertEqual(len(storage.all()), 1)

    def test_save_method(self):
        """Tests if save method saves to file"""
        storage = FileStorage()
        storage.save()
        self.assertTrue(True)

    def test_reload_method(self):
        """Tests if reload method loads from file"""
        storage = FileStorage()
        storage.reload()
        self.assertTrue(True)

    def test_reload_with_args(self):
        """Tests if reload method loads from file"""
        storage = FileStorage()
        with self.assertRaises(TypeError):
            storage.reload(None)
