class Solution:
    def longestPalindrome(self,s):
        forwards = s
        backwards = forwards[::-1]
        letterpos = 0
        backwardsletterpos = len(s)
        bestlength = 0
        total = ''
        for letter in forwards:
            count = 0
            for backwardsletter in backwards:
                count+=1
                if backwardsletter == letter:
                    if (len(backwards[(count - 1):backwardsletterpos]) >= bestlength):
                        if (backwards[(count - 1):backwardsletterpos] == forwards[letterpos:(len(s) - (count - 1))]):
                            total = backwards[(count - 1):backwardsletterpos]
                            bestlength = len(backwards[(count - 1):backwardsletterpos])
            letterpos+=1
            backwardsletterpos-=1
        if total == '':
            return s[0]
        else:
            return total


a = Solution()
print(a.longestPalindrome('eeeeeeeeeeeeeeeeeeeee'))
print(a.longestPalindrome('hello'))

# def longestPalindrome(s):
#     forwards = s
#     backwards = forwards[::-1]
#     letterpos = 0
#     backwardsletterpos = len(s)
#     bestlength = 0
#     total = ''
#     for letter in forwards:
#         # temp = []
#         count = 0
#         for backwardsletter in backwards:
#             count+=1
#             if backwardsletter == letter:
#                 # temp.append(count - 1) # zero indexed
#                 if (len(backwards[(count - 1):backwardsletterpos]) >= bestlength):
#                     if (backwards[(count - 1):backwardsletterpos] == forwards[letterpos:(len(s) - (count - 1))]):
#                         total = backwards[(count - 1):backwardsletterpos]
#                         bestlength = len(backwards[(count - 1):backwardsletterpos])
#         # print(temp)
#         # we have a temp, now see if backwards = forwards
#         # print(letterpos)
#         # print(backwardsletterpos)
#         # for (count - 1) in temp:
#             # print('forwarads: ' + backwards[(count - 1):backwardsletterpos])
#             # print('back: ' + forwards[letterpos:(len(s) - (count - 1))])
#             # print('length: ' + str(len(backwards[(count - 1):backwardsletterpos])))
#         letterpos+=1
#         backwardsletterpos-=1
#         # print('total is: ' + total)
#     if total == '':
#         return s[0]
#     else:
#         return total