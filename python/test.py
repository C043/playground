print("Hello World")


def productOrSum(num1: int, num2: int):
    if num1 * num2 >= 100:
        return num1 * num2
    else:
        return num1 + num2


print(productOrSum(1, 2))
print(productOrSum(50, 2))


def printSumInSequence(list: list):
    for idx, num in enumerate(list):
        print(num + list[idx - 1])


printSumInSequence([5, 5, 6, 5, 23, 5])


def displayEvenIndexCharactersFromInput():
    print("Write your senctence:")
    string: str = input()
    stringToPrint: str = ""

    for idx, char in enumerate(string):
        if idx % 2 == 0:
            stringToPrint = stringToPrint + char

    print(stringToPrint)


displayEvenIndexCharactersFromInput()


def listAndTupleFromInput(*arg):
    return list(arg), arg


array, frozenArray = listAndTupleFromInput(1, 5, 5, 7, 9)

print(array)
print(frozenArray)


def palindromChecker(string: str):
    if string == "":
        return False
    for idx, char in enumerate(string):
        idx = idx + 1
        if char != string[-idx]:
            return False
    return True


print(palindromChecker("itopinonavevanonipoti"))
print(palindromChecker(""))
print(palindromChecker("test"))


def sumAll(nums: list):
    sum: int = 0
    for num in nums:
        sum = sum + num
    return sum


print(sumAll([1, 5, 5, 7, 3, 4, 100]))


def countVowels(string: str):
    count: int = 0
    vowels: tuple = ("a", "e", "i", "o", "u")
    for char in string:
        if vowels.__contains__(char.lower()):
            count = count + 1
    return count


print(countVowels("aeiou"))
print(countVowels("Mario"))


def evenOrOdd(num: int):
    return num % 2 == 0


print(evenOrOdd(5))
print(evenOrOdd(2))
