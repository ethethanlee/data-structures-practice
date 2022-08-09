class Solution(object):
    def isPalindrome(self, s):
        left = 0
        right = len(s) -1
        while left < right:
            while not s[left].isalnum(): 
                left += 1
                if left == right:
                    return True
            while not s[right].isalnum(): 
                right -= 1
                if left == right:
                    return True
            lefty = s[left]
            righty = s[right]
            if lefty.isupper():
                lefty = lefty.lower()
            if righty.isupper():
                righty = righty.lower()
            if righty == lefty:
                right -=1
                left += 1
            else:
                return False
        return True

s = "0p"
sol = Solution()
print(sol.isPalindrome(s))