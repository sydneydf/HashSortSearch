import unittest

from Classes.Stem_Leaf import Stem_Leaf


class Test_Stem_Leaf(unittest.TestCase):
    def setUp(self):
        self.Stem_LeafObj = Stem_Leaf()

    def test_return_Stem_Leaf(self):
        # TODO: Temporary till Search is done
        self.assertEquals(self.Stem_LeafObj.tempPrintTest(), True)


if __name__ == '__main__':
    unittest.main()
