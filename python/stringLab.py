import string

translator = str.maketrans("", "", string.punctuation)

with open("randomText.txt") as infile:
    with open("outputText.txt", "w") as outfile:
        for line in infile:

            cleanLine: list = (
                line.lower().translate(translator).replace("—", "").split()
            )
            cleanedWords: str = "\n".join(cleanLine)

            outfile.write(cleanedWords)
