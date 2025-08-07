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
