def replaceWhiteSpaceWithDashes(string: str):
    words: list = string.split()
    return "-".join(words)


print(replaceWhiteSpaceWithDashes("Testing things out a little bit"))

print("(name, date),\n".strip("\n)(,"))

print("i got rejected".endswith("rejected"))
print("i got rejected".find("rejected"))

x: list = ['"abc"', "dfg", "hlmo", '"opxyz"']

for idx, string in enumerate(x):
    x[idx] = string.replace('"', "")

print(x)

string: str = "Mississippi"

lastIndexOfP: int = string.rindex("p")

convertedString: list = list(string)
convertedString[lastIndexOfP] = ""
newString: str = "".join(convertedString)
print(newString)
