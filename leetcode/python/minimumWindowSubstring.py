from collections import defaultdict


class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        # Return if the inputs are incorrect
        if not t or len(s) < len(t):
            return ""

        # Populate a frequentMap for the target
        targetFreqMap = defaultdict(int)
        for char in t:
            targetFreqMap[char] += 1

        # Create a frequency map for the window
        # We'll need this to count the frequencies of the chars in the current window
        windowMap = defaultdict(int)

        # Required is the lenght of the distinct chars in the target
        required = len(targetFreqMap)

        # formed is the length of the target right frequency of the target chars in the current window
        formed = 0

        # Initialize minLen to infinity
        minLen = float("inf")

        # These two variables are the best left and right indeces by the end these will tell us the best minimum window substring
        bestLeft = 0
        bestRight = 0

        # Initialize left as 0 (the first char in the string)
        left = 0

        # Loop the string once
        for right, char in enumerate(s):
            # We add the current char to the window frequency map
            windowMap[char] += 1

            # If the current char is in the target map and the frequency of it in the current window is equal to the target frequency, we add one to the formed counter
            if char in targetFreqMap and windowMap[char] == targetFreqMap[char]:
                formed += 1

            # When we have a good window, we reduce it moving left to the right until we don't have a good window anymore
            while formed == required:
                # We update the minimum window if it's smaller than the last one
                if right - left + 1 < minLen:
                    minLen = right - left + 1
                    bestLeft = left
                    bestRight = right

                # We reduce the window removing the frequency of the left chars that are no longer in it
                drop = s[left]
                windowMap[drop] -= 1
                if drop in targetFreqMap and windowMap[drop] < targetFreqMap[drop]:
                    formed -= 1

                # We move left to the right
                left += 1

        # By the end of the loop, we have the smallest substring, but if minLen is still infinity, it means that there is no minimum window substring so we return ""
        if minLen == float("inf"):
            return ""

        return s[bestLeft : bestRight + 1]


solution = Solution()
print(solution.minWindow("ADOBECODEBANC", "ABC"))
# print(solution.minWindow("A", "A"))

"""
This implementation is O(n) time complexity we loop over the strings only once
O(n) space complexity because we save everything in the maps
"""
