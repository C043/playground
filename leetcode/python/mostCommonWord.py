from collections import Counter
import re


class Solution:
    def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:
        # Remove punctuation from the paragraph and lower it
        normalized = "".join(
            character.lower() if character.isalnum() else " " for character in paragraph
        )
        # Convert banned in a set
        bannedSet = set(banned)
        # Use a map to count each word appearance, skipping banned words
        counts = Counter(word for word in normalized.split() if word not in bannedSet)
        # Return the word with most appearances
        return counts.most_common(1)[0][0]


string = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]

solution = Solution()
print(solution.mostCommonWord(string, banned))
