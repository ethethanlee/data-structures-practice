from collections import deque
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = deque()
        marker = 0
        for letter in s:
            if letter == '(' or letter == '{' or letter == '[':
                stack.append(letter)
                marker += 1
            else:
                if marker > 0:
                    temp = stack.pop()
                    marker -= 1
                    if temp == '(' and letter == ')':
                        continue
                    if temp == '{' and letter == '}':
                        continue
                    if temp == '[' and letter == ']':
                        continue
                    else:
                        return False
                else:
                    return False
        if stack:
            return False
        else:
            return True

s = "(]"
sol = Solution()
print(sol.isValid(s))