import unittest

from Classes.Sorter import Sorter
from sampleInput import sampleInput


# To Test our Sorter Class
class Test_InitialSort(unittest.TestCase):
    def setUp(self):
        self.TestObj = Sorter()

    # Compare to built in python function that returns sorted list from parsed in parameter
    def test_sorter(self):
        self.assertEqual(self.TestObj.bubble_sort(), sorted(sampleInput))


if __name__ == '__main__':
    unittest.main()
