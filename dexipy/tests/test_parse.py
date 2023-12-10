import unittest
from dexipy.parse import dexi_bool, dexi_vector, dexi_value, dexi_option_value


class test_test_parse(unittest.TestCase):

    def test_dexi_bool(self):
        self.assertFalse(dexi_bool(None))
        self.assertFalse(dexi_bool(""))
        self.assertFalse(dexi_bool([]))
        self.assertFalse(dexi_bool(0))
        self.assertFalse(dexi_bool(1))
        self.assertFalse(dexi_bool("F"))
        self.assertFalse(dexi_bool("tru"))
        self.assertTrue(dexi_bool("true"))
        self.assertTrue(dexi_bool("TRUE"))
        self.assertTrue(dexi_bool("True"))
        self.assertTrue(dexi_bool("t"))
        self.assertTrue(dexi_bool("T"))
        self.assertTrue(dexi_bool("1"))

    def test_dexi_vector(self):
        with self.assertRaises(AttributeError):
            dexi_vector(None)
        with self.assertRaises(AttributeError):
            dexi_vector([])
        with self.assertRaises(AttributeError):
            dexi_vector(1)
        with self.assertRaises(AttributeError):
            dexi_vector([1])
        with self.assertRaises(AttributeError):
            dexi_vector([1, 2])
        with self.assertRaises(AttributeError):
            dexi_vector(["1", "2"])
        with self.assertRaises(ValueError):
            dexi_vector("a")
        with self.assertRaises(ValueError):
            dexi_vector("1.1;5.5;-7.7xs")
        with self.assertRaises(ValueError):
            dexi_vector("")
        self.assertEqual(dexi_vector("1"), [1])
        self.assertEqual(dexi_vector("1.1"), [1.1])
        self.assertEqual(dexi_vector("1;2"), [1, 2])
        vec = dexi_vector("1;5;-7")
        self.assertEqual(vec, [1, 5, -7])
        self.assertTrue(isinstance(vec[0], int))
        vec = dexi_vector("1.1;5;-7.2")
        self.assertEqual(vec, [1.1, 5, -7.2])
        self.assertTrue(isinstance(vec[0], float))
        self.assertFalse(isinstance(vec[0], int))
        self.assertTrue(isinstance(vec[1], int))

    def test_dexi_value(self):
        with self.assertRaises(AttributeError):
            dexi_value([])
        self.assertIsNone(dexi_value(None))
        self.assertIsNone(dexi_value(""))
        self.assertIsNone(dexi_value("Undefined"))
        self.assertEqual(dexi_value("*"), "*")
        self.assertEqual(dexi_value("1"), 1)
        self.assertEqual(dexi_value("1", 1), 2)
        self.assertEqual(dexi_value("1:3"), {1, 2, 3})
        self.assertEqual(dexi_value("1:3", 2), {3, 4, 5})
        self.assertEqual(dexi_value("<1.1>"), [1.1])
        self.assertEqual(dexi_value("<1.1;2.2>"), [1.1, 2.2])
        self.assertEqual(dexi_value("{1;2}"), {1, 2})
        self.assertEqual(dexi_value("{1;2}", add = 1), {2, 3})
        self.assertEqual(dexi_value("{1; 5; -7}"), {1, 5, -7})
        self.assertEqual(dexi_value("{1; 5; -7}", 2), {3, 7, -5})
        self.assertEqual(dexi_value("<1.1; 5.5; -7.7>", 2), [1.1, 5.5, -7.7])

    def test_dexi_option_value(self):
        with self.assertRaises(AttributeError):
            dexi_option_value([])
        self.assertIsNone(dexi_option_value(None))
        self.assertIsNone(dexi_option_value("Undefined"))
        self.assertEqual(dexi_option_value(""), "*")
        self.assertEqual(dexi_option_value("*"), "*")
        self.assertEqual(dexi_option_value("1"), 1)
        self.assertEqual(dexi_option_value("12"), {1, 2})
        self.assertEqual(dexi_option_value("13334"), {1, 3, 4})

if __name__ == '__main__':
    unittest.main()
