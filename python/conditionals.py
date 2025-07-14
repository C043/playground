x = [1, 3, 5, 0, -1, 3, -2]


def removeAllNegatives(ls: list):
    for idx, num in enumerate(ls):
        if num < 0:
            del ls[idx]
    return ls


print(removeAllNegatives(x))

y = [[1, -1, 0], [2, 5, -9], [-2, -3, 0]]


def countTotalNumberOfNegativeNumbers(ls: list):
    count: int = 0
    for list in ls:
        for num in list:
            if num < 0:
                count += 1
    return count


print(countTotalNumberOfNegativeNumbers(y))


def howMuchHighIsTheNum(num: int):
    if num < -5:
        print("very low")
    elif num >= -5 and num <= 0:
        print("low")
    elif num == 0:
        print("neutral")
    elif num > 0 and num <= 5:
        print("high")
    else:
        print("very high")


howMuchHighIsTheNum(50)
