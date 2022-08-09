import math, time

class Solution(object):
    def convert(self, s, numRows):
        output = ''
        for i in range(math.ceil(numRows/2)): #for each row
            # print(i)
            n = 0 # prev number
            print('RESETTING N')
            it = False
            while (i + n + (2*(numRows - i) - 2)) <= len(s):
                print(i)
                output += s[i + n + (2*(numRows - i) - 2)]
                print('n = ' + str(n))
                print('s of ' + str(i + n*(2*(numRows - i) - 2)))
                n = i + n + (2*(numRows - i) - 2)
                if (numRows%2 == 0) & (i > 0) & (it == True):
                    print('n = ' + str(n))
                    print('2. s of ' + str(i + n + (2*(numRows - (i + 1)) - 2)))
                    output += s[int(i + n + (2*(numRows - (i + 1)) - 2))]
                    print('i = ' + str(i))
                    # n += 1
                it = True
                print(output)
        for i in range(math.ceil(numRows/2), numRows):
            n = 0
            # print(i)
            while (i + n*(2*(numRows - (numRows - (i + 1))) - 2)) < len(s):
                output += s[i + n*(2*(numRows - (numRows - (i + 1))) - 2)]
                n += 1
                # print(output)
            

        return output


sol = Solution()
print(sol.convert("PAYPALISHIRING", 4)) #now need to change it for 4+


        # theres gonna be a 2 since the top and bot rows count as 1 for teh zig zag