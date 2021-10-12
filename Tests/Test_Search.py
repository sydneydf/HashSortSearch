import unittest

from Classes.Search import Search


class TestSearch(unittest.TestCase):
    def setUp(self):
        self.SearchObj = Search()

    def test_searching(self):
        # We test search function
        self.assertEqual(self.SearchObj.search(125), 3)
        # Head to Search class for string dunder
        print(self.SearchObj)


if __name__ == '__main__':
    unittest.main()
