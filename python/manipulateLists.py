dataList: list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def pullLastThreeElements(array: list):
    arrayToReturn: list = array[-3:]
    del array[-3:]
    arrayToReturn.extend(array)
    return arrayToReturn


print(pullLastThreeElements(dataList))

listOfLists: list = [[1, 2, 3], [2, 1, 3], [4, 0, 1]]


def orderBySecondEl(array: list):
    return array[1]


# These two are the same
listOfLists.sort(key=orderBySecondEl)
listOfLists.sort(key=lambda lis: lis[1])
print(listOfLists)

duplicatedList: list = [1, 1, 5, 1]


def removeIfDuplicate(array: list, value):
    if array.count(value) > 1:
        while value in array:
            del array[array.index(value)]


removeIfDuplicate(duplicatedList, 1)
print(duplicatedList)
