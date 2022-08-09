s = "dvdf"

def lengthsub(blurb):
    here = ""
    counter = 0
    ohh = 0
    while blurb is not "":
        if blurb == "":
            if ohh < counter:
                ohh = counter   
            return ohh
        if blurb[:1] in here:
            if ohh < counter:
                ohh = counter
            while blurb[:1] in here:
                counter = counter - 1
                here = here[1:]   
        else:   
            counter += 1
            here += blurb[:1]
            blurb = blurb[1:]
    if ohh < counter:
        ohh = counter
    return ohh




print(lengthsub(s))

# new_string = blurb[1:]