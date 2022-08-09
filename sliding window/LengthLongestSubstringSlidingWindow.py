
class Solution(object):
    def LongestSubstring(self, s):
        letters = ''
        total = 0
        for lett in s:
            if lett in letters:
                if len(letters) > total:
                    total = len(letters)
                letters = lett
            else:
                letters = letters + lett
        if len(letters) > total:
            total = len(letters)
        return total

sol = Solution()
print(sol.LongestSubstring('abcabcbbbbbbb'))

# this was uneeded and also incorrect
