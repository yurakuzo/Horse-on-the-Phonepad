import unittest
from HorseOnPhonepad import hops_map, get_positions, count_hops


class TestGetHopPositions(unittest.TestCase):
    
    def test_get_positions_success(self):
        actual = get_positions(1)
        expected = (6, 8)
        self.assertEqual(actual, expected)

    def test_get_positions_success(self):
        actual = get_positions(4)
        expected = (3, 9, 0)
        self.assertEqual(actual, expected)

    def test_get_positions_exception(self):
        with self.assertRaises(ValueError) as exception_context:
           get_positions(-1)
        self.assertEqual(
            str(exception_context.exception),
            "There is no -1 on phonepad"
        )

    def test_get_positions_exception(self):
        with self.assertRaises(ValueError) as exception_context:
           get_positions(-10)
        self.assertEqual(
            str(exception_context.exception),
            "There is no -10 on phonepad"
        )

# class TestCountHops(unittest.TestCase):
    def test_count_hops_success(self):
        actual = count_hops(6, 5)
        expected = 86
        self.assertEqual(actual, expected)

    def test_count_hops_exception(self):
        with self.assertRaises(TypeError) as exception_context:
            count_hops(7)
        self.assertEqual(
            str(exception_context.exception),
            "count_hops() missing 1 required positional argument: 'hops'"
        )

    def test_count_hops_success(self):
        actual = count_hops(1, 2)
        expected = 5
        self.assertEqual(actual, expected)

    def test_count_hops_success(self):
        actual = count_hops(5, 4)
        expected = 0
        self.assertEqual(actual, expected)

    def test_count_hops_success(self):
        actual = count_hops(4, 3)
        expected = 17
        self.assertEqual(actual, expected)


    
