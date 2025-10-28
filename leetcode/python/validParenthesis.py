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

"""
This implementation is O(n) in time and space complexity because it loops over all the parenthesis in the string and it possibly saves them all in the stack if there are opened parenthesis only.

We define a dict with key closed parenthesis and value its opened counterpart.
We start a stack
We loop over all the chars in the string and if the char is opened, we add it to the stack, if it's closed, we check the last added parenthesis in the stack, if they don't match, we return false.

At the end we return whether if the stack is empty or not, if it's empty, it means that the parenthesis are valid.
"""
