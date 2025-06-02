# coding: ascii

import unittest
from core.cell import Cell


class TestCell(unittest.TestCase):
    def test_initial_state_default(self):
        cell = Cell()
        self.assertEqual(cell.get_state(), 0)

    def test_initial_state_custom(self):
        cell = Cell(42)
        self.assertEqual(cell.get_state(), 42)

    def test_set_state_valid(self):
        cell = Cell()
        cell.set_state(100)
        self.assertEqual(cell.get_state(), 100)

    def test_init_invalid_type(self):
        with self.assertRaises(TypeError):
            Cell("not an int")

    def test_set_state_invalid_type(self):
        cell = Cell()
        with self.assertRaises(TypeError):
            cell.set_state(3.14)

        with self.assertRaises(TypeError):
            cell.set_state("123")

        with self.assertRaises(TypeError):
            cell.set_state(None)

        with self.assertRaises(TypeError):
            cell.set_state(True)

        with self.assertRaises(TypeError):
            cell.set_state([1, 2, 3])


if __name__ == "__main__":
    unittest.main()
