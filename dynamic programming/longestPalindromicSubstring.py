def longestPalindrome(s):
    """
    :type s: str
    :rtype: str
    """
    # does not work
    counter = 0
    where = 0
    length = 0
    total = ''
    temp = ''
    for letter in s: ## get it backwards
        temp = letter + temp
    for letter in s: ## try to find a palindrome for each letter that there is?
        where = temp.find(letter) ## this si fucked up rn - need to find all of them

        if (len(s) == 1):
            return s
        
        if (len(s) - where - 1) == counter:
            counter += 1
            continue

        if ((temp[where : len(s) - counter]) == (s[counter : (len(s) - where)])) & (len(temp[where : len(s) - counter]) > length):
            total = temp[where : len(s) - counter]
            length = len(temp[where : len(s) - counter])

        

        counter += 1


    if total == '':
        return s[0]
    else:
        return total

# NEED TO ACCOUNT FOR WHEN PALINDROME IS INSIDE STUFF

print(longestPalindrome('superpieceofshit'))