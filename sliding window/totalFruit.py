from collections import defaultdict


class Solution(object):
    def totalFruit(self, fruits):
        listo = []
        longestLength = 2
        if len(fruits) < 3:
            return len(fruits)
        listo = fruits[0:(2)]
        i = 0
        iCounter = 0
        while i < (len(fruits) - 2):
            print(listo)
            if fruits[i+2] in listo or all(ele == listo[0] for ele in listo):
                if all(ele == listo[0] for ele in listo):
                    iCounter += 1
                else:
                    pass
                listo.append(fruits[i+2])
                if len(listo) > longestLength:
                    longestLength = len(listo)
                i += 1
            else:
                i = i+3-len(listo) + iCounter
                listo = fruits[i:i+2]
                iCounter = 0
            print(listo)
            print('---------- + ' + str(iCounter))
        return longestLength

    def totalFruitSol(self, tree) -> int:
        ans = 0
        count = defaultdict(int)

        l = 0
        for r, t in enumerate(tree):
            count[t] += 1
            while len(count) > 2:
                count[tree[l]] -= 1
                if count[tree[l]] == 0:
                    del count[tree[l]]
                l += 1
            ans = max(ans, r - l + 1) #r is count and t is the value

        return ans

sol = Solution()
print(sol.totalFruitSol([3,3,3,1,2,1,1,2,3,3,4]))
            