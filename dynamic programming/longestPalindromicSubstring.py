class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        output = ""
        i = 0
        while i < len(s):
            output = max(self.palin(s,i,i), self.palin(s,i,i+1), output, key=len)
            #the two helpers are offset by 1!!!
            i+=1

        return output
       
        
    def palin(self,s,left,right):
        while 0<=left and right < len(s) and s[left]==s[right]:
                left-=1; right+=1
        return s[left+1:right]

sol = Solution()
print(sol.longestPalindrome('babad'))

#for dynamic programming, offset by 1