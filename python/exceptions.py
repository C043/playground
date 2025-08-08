try:
    print("First number of the division")
    num1 = float(input())
    print("Second number of the division")
    num2 = float(input())

    division = num1 / num2
except ZeroDivisionError:
    print("Second number cannot be zero!")
except:
    print("There was an error")
else:
    print(f"The result was {division}")

print("Type a number different from Zero")
num = float(input())
assert num != 0, "Number is zero"


class ValueTooLarge(Exception):
    pass


try:
    print("Give me a less than 1000 number")
    num = float(input())
    if num > 1000:
        raise ValueTooLarge
except ValueTooLarge:
    print("Value more than 1000")
