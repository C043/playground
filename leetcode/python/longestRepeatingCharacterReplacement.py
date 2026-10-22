class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        left = highestCount = best = 0

        for right, char in enumerate(s):
            count[char] = count.get(char, 0) + 1

            highestCount = max(highestCount, count[char])

            while (right - left + 1) - highestCount > k:
                count[s[left]] -= 1
                left += 1

            best = max(best, right - left + 1)

        return best


s = "ABAB"
k = 2
solution = Solution()
print(solution.characterReplacement(s, k))
