# @leet start
from collections import defaultdict


class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        grouped = defaultdict(list)

        for word in strs:
            key = "".join(sorted(word))
            grouped[key].append(word)

        return list(grouped.values())


solution = Solution()
print(solution.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))


# @leet end

"""
This implementation is O(n x n log k) in time complexity because we loop once through the entire input list, but we sort each string in place
It's O(n x k) in space complexity too because we save all the values and keys in a dict
"""
