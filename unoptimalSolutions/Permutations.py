import math
def perm(term):
    n = 0
    ans = 1
    word = ""
    for character in term:
        n = n + 1
        m = 0
        if character in word: # ok so if there is a same letter then we should probably make a new variable and start it at 2
            #count number of occurrences of that letter then divide some variable that starts at 1 by the (number of occurences)!
            pass
        else:
            for letter in term:
                if character == letter:
                    m = m + 1
                # scan thru and see how many there are!!!
            ans = ans/(math.factorial(m)) #thing needs to be the amount of times the character comes up in the word
        word = character + word
    return(ans*math.factorial(n))
term = input("What is the word?\n")
print(perm(term))
