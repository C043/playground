# @leet start


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        pairs = {")": "(", "]": "[", "}": "{"}

        for i in s:
            if i in pairs.values():
                stack.append(i)
            elif i in pairs:
                if not stack or stack[-1] != pairs[i]:
                    return False

                stack.pop()

        return len(stack) == 0


solution = Solution()
print(solution.isValid("([])"))

# @leet end
