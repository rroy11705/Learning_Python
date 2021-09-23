# small class function normal --> addition, sub, mul

# python -m unittest test_module test_upper
# python -m unittest test_module.TestClass
# python -m unittest test_module.TestClass.test_method

import unittest


class TestExample(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('andre'.upper(), 'ANDRE')

    def test_isupper(self):
        self.assertTrue('ANDRE'.isupper())
        self.assertFalse('andre'.isupper())

    def test_split(self):
        s = 'Hello world'
        self.assertEqual(s.split(), ['Hello', 'world'])


if __name__ == '__main_':
    unittest.main()
