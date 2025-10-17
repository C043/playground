# @leet start


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        splitted = list(s)

        if len(splitted) <= 1:
            return False

        opened = []

        for char in splitted:
            if char == "{" or char == "[" or char == "(":
                opened.append(char)
            else:
                if len(opened) == 0:
                    return False

                lastOpened = opened.pop()
                if char == "}" and lastOpened != "{":
                    return False
                elif char == "]" and lastOpened != "[":
                    return False
                elif char == ")" and lastOpened != "(":
                    return False

        if len(opened) > 0:
            return False

        return True


solution = Solution()
print(solution.isValid("([])"))

# @leet end
