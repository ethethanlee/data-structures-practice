
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        setofdict = []
        output = []
        for item in strs:
            temp = {}
            for letter in item:
                if letter in temp:
                    temp[letter] += 1
                else:
                    temp[letter] = 1
            if temp in setofdict:
                output[setofdict.index(temp)].append(item)
            else:
                setofdict.append(temp)
                output.append([item])
        return output

sol = Solution()
print(sol.groupAnagrams(strs = ['']))