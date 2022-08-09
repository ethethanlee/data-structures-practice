class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        output = 2
        total = 0
        if len(fruits) < 3:
            return len(fruits)
        for i in range(len(fruits) - 2):
            if fruits[i+2] in fruits[i:(i+2)]:
                output += 1
                if total < output:
                    total = output
            else:
                if total < output:
                    total = output
                output = 2

        return total


sol = Solution()
print(sol.totalFruit([0,1,1,2]))