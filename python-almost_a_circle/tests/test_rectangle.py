#!/usr/bin/python3
"""unittests for the Rectangle class"""
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """tests for the Rectangle class"""

    def test_constructor(self):
        rect = Rectangle(1, 2)
        self.assertEqual(rect.id, 1)
        self.assertEqual(rect.width, 1)
        self.assertEqual(rect.height, 2)
        self.assertEqual(rect.x, 0)
        self.assertEqual(rect.y, 0)

    def test_string_representation(self):
        rect = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(str(rect), "[Rectangle] (5) 3/4 - 1/2")

    def test_area(self):
        rect = Rectangle(3, 4)
        self.assertEqual(rect.area(), 12)

    def test_display(self):
        rect = Rectangle(2, 2)
        expected_output = "##\n##\n"
        with unittest.mock.patch("sys.stdout", new_callable=io.StringIO) as mock_stdout:
            rect.display()
            self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_update(self):
        rect = Rectangle(1, 2, 3, 4, 5)
        rect.update(6, 7, 8, 9, 10)
        self.assertEqual(rect.id, 6)
        self.assertEqual(rect.width, 7)
        self.assertEqual(rect.height, 8)
        self.assertEqual(rect.x, 9)
        self.assertEqual(rect.y, 10)

    def test_update_kwargs(self):
        rect = Rectangle(1, 2, 3, 4, 5)
        rect.update(id=6, width=7, height=8, x=9, y=10)
        self.assertEqual(rect.id, 6)
        self.assertEqual(rect.width, 7)
        self.assertEqual(rect.height, 8)
        self.assertEqual(rect.x, 9)
        self.assertEqual(rect.y, 10)

    def test_to_dictionary(self):
        rect = Rectangle(1, 2, 3, 4, 5)
        expected_dict = {
            "id": 5,
            "width": 1,
            "height": 2,
            "x": 3,
            "y": 4,
        }
        self.assertEqual(rect.to_dictionary(), expected_dict)


if __name__ == "__main__":
    unittest.main()
