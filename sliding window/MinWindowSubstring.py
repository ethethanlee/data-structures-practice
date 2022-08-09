from collections import defaultdict
import math

class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        output = ''
        count = math.inf
        if len(t) > len(s):
            return ''
        window = ''
        tdict = defaultdict(int)
        for letter in t:
            tdict[letter] += 1
        print(tdict)
        notables = defaultdict(int)
        for currentletter in s:
            window += currentletter
            print (window)
            if currentletter in t:
                notables[currentletter] += 1
                # will have to say if every value of notables is greater than or equal
            shared = {k: notables[k] for k in notables if k in tdict and notables[k] >= tdict[k]}
            while len(shared) == len(tdict) == len(notables):
                if count > len(window):
                    count = len(window)
                    output = window
                temp = window[0]
                window = window[1:]
                if temp in notables:
                    notables[temp] -= 1
                shared = {k: notables[k] for k in notables if k in tdict and notables[k] >= tdict[k]}
        return output

sol = Solution()
print(sol.minWindow('ADOBECODEBANC', 'ABC'))