import time

from sampleInput import sampleInput as _sampleList


class Sorter:
    # WE are going to cheat and use a simpler sorting algorithm to implement, Bubble sort.
    # quicksort will take longer to implement.
    def __init__(self):
        # Class initialized by importing unsorted list from /sampleInput.py
        self.sampleList = _sampleList

    def bubble_sort(self):
        # Record amount
        swap_count = 0
        # With this loop we start at the full length of list end goal of reaching 0, each iteration decrease by 1
        # equates to range(133 as the start, 0 to be the end and each loop take 1 away till end
        for x in range(len(self.sampleList) - 1, 0, - 1):
            # get current x and pass into 2nd layer for
            for y in range(x):
                # compare current to the next index of sampleList

                # Swapping occurs via variable packing
                # self.sampleList[y], self.sampleList[y + 1] = self.sampleList[y + 1], self.sampleList[y]
                if self.sampleList[y] > self.sampleList[y + 1]:
                    self.sampleList[y], self.sampleList[y + 1] = self.sampleList[y + 1], self.sampleList[y]
                    swap_count += 1
                    #TODO: UNCOMMENT AFTER STEM_LEAF FINISHED print(f"Swapping Operations count: {swap_count}")

        # Silly Print
        # TODO: UNCOMMENT AFTER STEM_LEAF FINISHED
        # print("As you can see even though bubble sort is the quickest to code...")
        # for x in range(3):
        #     time.sleep(1)
        #     print("." * x)
        #     if x == 2:
        #         print("It is probably the most inefficient")

        return self.sampleList
