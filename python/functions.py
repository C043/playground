x = 5


def funct_1():
    x = 3


def funct_2():
    global x
    x = 2


funct_1()


funct_2()

print(x)
