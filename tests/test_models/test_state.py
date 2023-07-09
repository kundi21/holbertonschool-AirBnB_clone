#!/usr/bin/python3
"""Unittest for models/state.py"""
import unittest
from models.state import State


class to_Test_State(unittest.TestCase):
    """Class to test State class"""

    def test_state_instance(self):
        """Test if instance is created"""
        state = State()
        self.assertIsInstance(state, State)

    def test_state_name_str(self):
        """Test if name is correct"""
        state = State()
        self.assertIsInstance(state.name, str)

    def test_state_created_at_str(self):
        """Test if created_at is str"""
        state = State()
        self.assertIsInstance(state.created_at, str)

    def test_state_updated_at_str(self):
        """Test if updated_at is str"""
        state = State()
        self.assertIsInstance(state.updated_at, str)

    def test_state_id_str(self):
        """Test if id is str"""
        state = State()
        self.assertIsInstance(state.id, str)

class to_Test_State_save(unittest.TestCase):
    """Class to test save method of State class"""

    def test_state_save_created_at(self):
        """Test if created_at is updated"""
        state = State()
        state.save()
        self.assertNotEqual(state.created_at, state.updated_at)

    def test_state_save_with_arg(self):
        """Test if save with arg"""
        state = State()
        with self.assertRaises(TypeError):
            state.save(None)

class to_Test_State_to_dict(unittest.TestCase):
    """Class to test to_dict method of State class"""

    def test_state_to_dict_dict(self):
        """Test if to_dict returns a dictionary"""
        state = State()
        self.assertIsInstance(state.to_dict(), dict)

    def test_state_to_dict_with_arg(self):
        """Test if to_dict with arg"""
        state = State()
        with self.assertRaises(TypeError):
            state.to_dict(None)
