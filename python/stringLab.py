import string

with open("randomText.txt") as infile:
    with open("outputText.txt", "w") as outfile:
        for line in infile:
            translator = str.maketrans("", "", string.punctuation)

            cleanLine: list = (
                line.lower().translate(translator).replace("—", "").split()
            )
            for word in cleanLine:
                outfile.write(f"{word}\n")
