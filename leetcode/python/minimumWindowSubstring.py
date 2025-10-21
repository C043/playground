from collections import defaultdict


class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if not t or len(s) < len(t):
            return ""

        targetFreqMap = defaultdict(int)
        for char in t:
            targetFreqMap[char] += 1

        windowMap = defaultdict(int)
        required = len(targetFreqMap)
        formed = 0

        minLen = float("inf")
        bestLeft = 0
        bestRight = 0

        left = 0

        for right, char in enumerate(s):
            windowMap[char] += 1

            if char in targetFreqMap and windowMap[char] == targetFreqMap[char]:
                formed += 1

            while formed == required:
                if right - left + 1 < minLen:
                    minLen = right - left + 1
                    bestLeft = left
                    bestRight = right

                drop = s[left]
                print(drop)
                windowMap[drop] -= 1
                if drop in targetFreqMap and windowMap[drop] < targetFreqMap[drop]:
                    formed -= 1

                left += 1

        if minLen == float("inf"):
            return ""

        return s[bestLeft : bestRight + 1]


solution = Solution()
print(solution.minWindow("ADOBECODEBANC", "ABC"))
# print(solution.minWindow("A", "A"))
