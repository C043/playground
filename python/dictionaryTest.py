nameAndAges: dict = {}

for num in range(1, 4):
    print(f"Name number {num}")
    name = input()
    print("How old is he/she?")
    age = input()

    nameAndAges[name] = age

print("Now ask me about one of those names, come on!")
name = input()
if name in nameAndAges:
    print(f"The age of {name} is {nameAndAges[name]}")
else:
    print(f"You think you're smart? You didn't tell me about {name}!")
