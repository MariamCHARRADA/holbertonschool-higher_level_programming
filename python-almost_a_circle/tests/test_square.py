#!/usr/bin/python3
"""unittests for the Square class"""
import unittest
from models.square import Square
import io
import sys


class TestSquare(unittest.TestCase):
    """tests for the Square class"""

    def test_constructor(self):
        square = Square(3)
        self.assertEqual(square.id, 1)
        self.assertEqual(square.size, 3)
        self.assertEqual(square.x, 0)
        self.assertEqual(square.y, 0)

    def test_string_representation(self):
        square = Square(2, 3, 4, 5)
        self.assertEqual(str(square), "[Square] (5) 3/4 - 2")

    def test_size_property(self):
        square = Square(2)
        self.assertEqual(square.size, 2)
        square.size = 4
        self.assertEqual(square.size, 4)
        self.assertEqual(square.width, 4)
        self.assertEqual(square.height, 4)

    def test_area(self):
        square = Square(3)
        self.assertEqual(square.area(), 9)

    def test_display(self):
        square = Square(2)
        expected_output = "##\n##\n"
        with io.StringIO() as mock_stdout, unittest.mock.patch(
            "sys.stdout", mock_stdout
        ):
            square.display()
            self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_update(self):
        square = Square(2, 3, 4, 5)
        square.update(6, 7, 8, 9)
        self.assertEqual(square.id, 6)
        self.assertEqual(square.size, 7)
        self.assertEqual(square.x, 8)
        self.assertEqual(square.y, 9)

    def test_update_kwargs(self):
        square = Square(2, 3, 4, 5)
        square.update(id=6, size=7, x=8, y=9)
        self.assertEqual(square.id, 6)
        self.assertEqual(square.size, 7)
        self.assertEqual(square.x, 8)
        self.assertEqual(square.y, 9)

    def test_to_dictionary(self):
        square = Square(2, 3, 4, 5)
        expected_dict = {"id": 5, "x": 3, "y": 4, "size": 2}
        self.assertEqual(square.to_dictionary(), expected_dict)


if __name__ == "__main__":
    unittest.main()
