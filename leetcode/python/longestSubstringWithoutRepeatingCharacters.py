class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        left = 0
        visited = set()
        maxLen = 0

        for right in range(len(s)):
            while s[right] in visited:
                visited.remove(s[left])
                left += 1

            visited.add(s[right])
            maxLen = max(maxLen, right - left + 1)

        return maxLen


solution = Solution()
print(solution.lengthOfLongestSubstring("abcabcbb"))

"""
This implementation is very important to understand sliding window pattern.
The time complexity is O(n) because we loop all the string once
The space complexity is O(o) where o is the size of the alphabet because at worst we save in the set all the alphabet if the string has a 26 long substring with different characters
"""
