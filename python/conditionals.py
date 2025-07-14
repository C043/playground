x = [1, 3, 5, 0, -1, 3, -2]


def removeAllNegatives(ls: list):
    for idx, num in enumerate(ls):
        if num < 0:
            del ls[idx]
    return ls


print(removeAllNegatives(x))
