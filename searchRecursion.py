# an example of recursive porgramming using binary search on a sorted list.
# has a teacher's solution bellow the main code.
def listSearch(sortedList, search, removedItems):
    length = len(sortedList)
    mini = length//2
    if sortedList[mini] == search:
        print(str(search), "is item", str(mini + removedItems), "in the sorted list")
    elif search > sortedList[mini]:
        removedItems += (length-mini)
        sortedList = sortedList[mini+1:]
        listSearch(sortedList, search, removedItems)
    elif search < sortedList[mini]:
        sortedList = sortedList[:mini]
        listSearch(sortedList, search, removedItems)

listSearch([1,2,3,4,5,6,7,8,9,10,11,12,13,14,18], 14, 0)
"""
total of mini's is the index so can be solved by adding minis up 
and returning it all each time instead of removedItems method.
"""
"""
TEACHER SOLUTION:
def binSearch(inputList, value):
    midIndex = len(inputList)//2
    if value == inputList[midIndex]:
        # if we land on the search value we return it's index in the list.
        return midIndex
    elif value < inputList[midIndex]:
        # slicing the list and by default does not include mid value.
        # recurs into itself and searches again
        binSearch(inputList[:midIndex], value)
    elid value > inputList[midIndex]:
        # this needs +1 as slicing includes the mid value this way but not the other.
        # recurs into itself and searches again
        binSearch(inputList[midIndex+1:], value)
"""