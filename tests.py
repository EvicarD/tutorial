import unittest
from functions import total
from functions import *

class TestCaseForFunctions(unittest.TestCase):
    def test_total(self):
        self.assertEqual(total(15), sum(range(15+1)))

if __name__ == '__main__':
    unittest.main()