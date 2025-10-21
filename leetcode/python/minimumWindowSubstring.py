class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        # If s length < t length return ""
        if len(s) < len(t):
            return ""
        # If s length = 1 and t length = 1 and they have the same char, return that char
        elif len(s) == 1 and len(t) == 1 and s[0] == t[0]:
            return s[0]

        # Initiate the frequency map for t
        targetFrequencyMap = {}
        # Initizte the target length
        currentWindowCounter = len(t)

        # Popolate the frequency map looping t
        for char in t:
            targetFrequencyMap.setdefault(char, 0)
            targetFrequencyMap[char] = targetFrequencyMap[char] + 1

        # Initiate the current window frequency map for s
        currentWindowFrequencyMap = {}

        # Initiate the two window pointers
        left = 0
        right = 0

        # Initiate the minimum window substring to ""
        minSubstring = ""
        # Initiate the current window substring to ""
        currentWindowSubstring = ""

        # Loop through s with the window once
        for chars in s:
            s[right]
        # Return the minimum substring


solution = Solution()
print(solution.minWindow("ADOBECODEBANC", "ABC"))
