def replaceWhiteSpaceWithDashes(string: str):
    words: list = string.split()
    return "-".join(words)


print(replaceWhiteSpaceWithDashes("Testing things out a little bit"))
