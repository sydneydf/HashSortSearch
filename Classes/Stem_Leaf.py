from Classes.Sorter import Sorter


class Stem_Leaf:
    def __init__(self):
        self.sortedList = []
        self.stemLeafDict = {}
        self.initClsSetup()

    def initClsSetup(self):
        self.sortedList = Sorter().bubble_sort()

        # initialize and pregen 15 stem keys because our max nums from file is 150
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

    # ON UNITTESTS THIS PRINTS NORMALLY
    def tempPrintTest(self):
        # Was tempted to use Stempgraphic package with numpy here but I thought that might be cheating

        # proper print aligning with string justify methods
        print("STEM", "|Leaf".rjust(5, " "))

        # variable unpack dictionary
        # also using end= paramater to print on same line
        for stem, leafList in self.stemLeafDict.items():
            print(stem, end=" ")

            # Spacefix created to properly align 2 digit stems for print
            spaceFix = 4
            if len(str(stem)) > 1:
                spaceFix -= 1
            # Implementing spacefix with justify prints
            print("|".rjust(spaceFix, " "), end=" ")
            for leaf in leafList:
                print(leaf, end=" ")
            # New line for next stemleaf
            print("\n")
        return True
