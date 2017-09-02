# Check out visualization of sorting here: https://www.cs.usfca.edu/~galles/visualization/ComparisonSort.html
# This package benchmars the speed of all of the sorting methods

import csv
import timeit
from collections import defaultdict
import gc
import matplotlib as plt

class Sort:
    def __init__(self, csvLoc):
        self.csvLoc = csvLoc

    def unsortedList(self):
        with open(sort.csvLoc, newline='') as f:
            reader = csv.reader(f)
            list_unsorted = []
            for row in reader:
                i = int(row[0])  # first column of the row
                list_unsorted.append(i)
            return list_unsorted

    # insertion sort:
    def insertionSort(self):
        list = sort.unsortedList()
        for index in range(1, len(list)):
            currentvalue = list[index]
            position = index

            while position > 0 and list[position - 1] > currentvalue:
                list[position] = list[position - 1]
                position = position - 1

            list[position] = currentvalue

        return list

    # bubbleSort
    def bubbleSort(self):
        list = sort.unsortedList()
        sorted = False
        while not sorted:
            sorted = True
            for index in range(0, len(list) - 1):
                current_value = list[index]
                next_position = list[index + 1]
                if current_value > next_position:
                    sorted = False
                    list[index] = next_position
                    list[index + 1] = current_value

        return list

    #using the built in python sort function
    def builtinSort(self):
        list = sorted(sort.unsortedList())
        return list


loop_limit = 5
sort = Sort("loanstats.csv")
sortDict = defaultdict(list)



for i in range(1,loop_limit):
    start = timeit.default_timer()
    sort.bubbleSort()
    stop = timeit.default_timer()
    print("bubbleSort ran in an average of " + str(((stop - start)/i )) + " seconds over " + str(i) + " loops.  Here is the output: ")
    print(sort.builtinSort())
    sortDict['bubbleSort'].append([(((stop - start)/i )), i])
    gc.collect()


for i in range(1,loop_limit):
    start = timeit.default_timer()
    sort.insertionSort()
    stop = timeit.default_timer()
    print("insertionSort ran in an average of " + str(((stop - start)/i )) + " seconds over " + str(i) + " loops.  Here is the output: ")
    print(sort.builtinSort())
    sortDict['insertionSort'].append([(((stop - start)/i )), i])
    gc.collect()

for i in range(1,loop_limit):
    start = timeit.default_timer()
    sort.builtinSort()
    stop = timeit.default_timer()
    print("builtinSort ran in an average of " + str(((stop - start)/i )) + " seconds over " + str(i) + " loops.  Here is the output: ")
    print(sort.builtinSort())
    sortDict['builtinSort'].append([(((stop - start)/i )), i])
    gc.collect()


print(sortDict)



