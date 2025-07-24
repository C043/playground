#! /usr/bin/env python3
"""
wc: count the number of lines, words and characters of a text file
python3 wc.py -i <inputTextFile> [options]

-l print line count only
-w print word count only
-c print character count only
-L print longest line length only
"""
import sys, string, argparse

translator = str.maketrans("", "", string.punctuation)


def main():
    parser = argparse.ArgumentParser(usage=__doc__)
    parser.add_argument(
        "-i", "--input", type=argparse.FileType("r"), help="Input file to read"
    )
    parser.add_argument("-l", "--lines", action="store_true")
    parser.add_argument("-w", "--words", action="store_true")
    parser.add_argument("-c", "--chars", action="store_true")
    parser.add_argument("-L", "--longest", action="store_true")
    args = parser.parse_args()

    lines: int = 0
    words: int = 0
    chars: int = 0
    longest: int = 0
    with args.input as file:
        for line in file:
            lineWords = len(line.split())

            lines = lines + 1
            words = words + lineWords
            chars = chars + len(line)

            if longest < lineWords:
                longest = lineWords

    if len(sys.argv) == 3 and args.input:
        print(f"Lines: {lines}")
        print(f"Words: {words}")
        print(f"Chars: {chars}")
        print(f"Longest line: {longest}")

    if args.lines:
        print(f"Lines: {lines}")
    if args.words:
        print(f"Words: {words}")
    if args.chars:
        print(f"Chars: {chars}")
    if args.longest:
        print(f"Longest line: {longest}")


if __name__ == "__main__":
    main()
else:
    print("wc loaded as a module")
