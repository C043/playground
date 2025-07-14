wordCountDict: dict = {}

with open("outputText.txt", "r") as infile:
    for word in infile:
        strippedWord = word.strip()

        wordCountDict.setdefault(strippedWord, 0)
        wordCountDict[strippedWord] += 1


sortedWords = sorted(list(wordCountDict.items()), key=lambda x: x[1])

print("Most common words:")
for word in reversed(sortedWords[-5:]):
    print(word)

print("\nLeast common words:")

for word in sortedWords[:5]:
    print(word)
