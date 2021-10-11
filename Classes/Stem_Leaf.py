from Classes.Sorter import Sorter


# TODO: This class needs major refinement once search is done.
# TODO: We use search to test if Stem_leaf is working
class Stem_Leaf:
    def __init__(self):
        self.sortedList = []
        self.stemLeafDict = {}
        self.initClsSetup()

    # TODO: Will this work?
    def initClsSetup(self):
        self.sortedList = Sorter().bubble_sort()
        # initialize and pregen 15 stem keys because our max nums from file is 150

        # TODO: Does return_Stem_Leaf() create keys ??
        for stem in range(15):
            self.stemLeafDict[stem] = []

        self.process2Stem_Leaf()

    def process2Stem_Leaf(self):
        for num in self.sortedList:
            # Grab last index of number
            potentialLeaf = int(str(num)[-1])

            # Using string slicing we can grab the beginning to digits and convert back to an int
            # NOTE: I know this is not very efficient but I love python slicing
            if len(str(num)) == 3:
                potentialStem = int(str(num)[:2])
            elif len(str(num)) == 2:
                potentialStem = int(str(num)[:1])
            else:
                potentialStem = 0

            # append Leaf to Stem Key
            self.stemLeafDict[potentialStem].append(potentialLeaf)

    def tempPrintTest(self):
        for stem, leafList in self.stemLeafDict.items():
            print(f"Stem: {stem}")
            for leaf in leafList:
                print(f"Leaf for stem {stem}: {leaf}")
        return True
