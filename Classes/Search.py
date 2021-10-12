from Classes.Stem_Leaf import Stem_Leaf


class Search():
    def __init__(self):
        self.Stem_LeafObj = Stem_Leaf()
        self.searchedInt = 0
        self.countOfLeaf = 0

    # special python magic method returns string when object treated as string
    def __str__(self):
        if self.countOfLeaf > 0:
            return f"We found {self.searchedInt} {self.countOfLeaf} times!!!"
        else:
            return "Have you tried searching yet?"

    def search(self, _int2Search):
        # store in object
        self.searchedInt = _int2Search

        # Copied from my stem_leaf class
        if len(str(self.searchedInt)) == 3:
            potentialStem = int(str(self.searchedInt)[:2])
        elif len(str(self.searchedInt)) == 2:
            potentialStem = int(str(self.searchedInt)[:1])
        else:
            potentialStem = 0

        # Head to corresponding stem by passing in key as index
        # then iterate over that corresponding list and retrieve count of values and internally store it
        potentialLeaf = int(str(self.searchedInt)[-1])
        for i in self.Stem_LeafObj.stemLeafDict[potentialStem]:
            if i == potentialLeaf:
                self.countOfLeaf += 1

        return self.countOfLeaf
