#!/usr/bin/python3
"""unittests for the Base class"""
import unittest
from models.base import Base
import os


class TestBase(unittest.TestCase):
    """tests for the Base class"""

    def test_to_json_string(self):
        data = [{"id": 1, "name": "Item1"}, {"id": 2, "name": "Item2"}]
        json_str = Base.to_json_string(data)
        self.assertEqual(type(json_str), str)
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_save_to_file(self):
        # Create an instance and save it to a file
        obj = Base(1)
        Base.save_to_file([obj])
        self.assertTrue(os.path.exists("Base.json"))

    def test_from_json_string(self):
        json_str = '[{"id": 1, "name": "Item1"}, {"id": 2, "name": "Item2"}]'
        data = Base.from_json_string(json_str)
        self.assertEqual(type(data), list)
        self.assertEqual(data, [{"id": 1, "name": "Item1"}, {"id": 2, "name": "Item2"}])

    def test_create(self):
        data = {"id": 1, "name": "Item1"}
        obj = Base.create(**data)
        self.assertEqual(obj.id, 1)
        self.assertEqual(obj.name, "Item1")

    def test_load_from_file(self):
        # Create a test data file with JSON data
        json_data = '[{"id": 1, "name": "Item1"}, {"id": 2, "name": "Item2"}]'
        with open("Base.json", "w") as file:
            file.write(json_data)

        instances = Base.load_from_file()
        self.assertEqual(len(instances), 2)
        self.assertEqual(instances[0].id, 1)
        self.assertEqual(instances[1].name, "Item2")



if __name__ == "__main__":
    unittest.main()
