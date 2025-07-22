from typing_extensions import clear_overloads


x = 5


def funct_1():
    x = 3


def funct_2():
    global x
    x = 2


funct_1()


funct_2()

print(x)


# decorators
def decorate(func):
    print("in decorate function, decoratind", func.__name__)

    def wrapperFunc(*args):
        print("Executing", func.__name__)
        cleaned_args = " ".join(str(arg) for arg in args)
        string = f"<html>{cleaned_args}</html>"
        return func(string)

    return wrapperFunc


@decorate
def myfunc(parameter):
    print(parameter)


myfunc("hello")
