def longestPalindrome(s):
    # this code didnt work rip
    """
    :type s: str
    :rtype: str
    """
    counter = 0
    where = 0
    length = 0
    total = ''
    temp = ''
    lets = []
    for letter in s: ## get it backwards
        temp = letter + temp
    for letter in s: ## try to find a palindrome for each letter that there is?
        if (len(s) == 1):
            return s

        movingtemp = temp
        cont = 0
        for alph in temp:
            if alph == letter:
                lets.append(movingtemp.index(alph) + cont)
                movingtemp = movingtemp[movingtemp.index(alph):]
                cont += movingtemp.index(alph)
                print(lets)
                print(movingtemp)
            if (len(s) - where - 1) == counter:
                counter += 1
                continue
            # print(letter)
            for n in lets:
                where = n
                # checks if its the same thing backwards
                # print(temp)
                # print((temp[where : len(s) - counter]))
                # print(s)
                # print((s[counter : (len(s) - where)]))
                # print("-------------")
                if ((temp[where : len(s) - counter]) == (s[counter : (len(s) - where)])) & (len(temp[where : len(s) - counter]) > length):
                    total = temp[where : len(s) - counter]
                    length = len(temp[where : len(s) - counter])

        
        # print(lets)

        

        counter += 1


    if total == '':
        return s[0]
    else:
        return total

# NEED TO ACCOUNT FOR WHEN PALINDROME IS INSIDE STUFF

print(longestPalindrome("abacab"))