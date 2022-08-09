l1 = [9,9,9,9,9,9,9]
l2 = [9,9,9,9]


def addd(l1, l2):
    thing = True
    l = []
    if len(l2) > len(l1):
        for n in range (len(l2)-len(l1)):
            l1.append(0)
        for i in range(len(l2)):
            unit = l1.pop(0)
            unitunit = l2.pop(0)
            if unit + unitunit < 10 and (not (unit + unitunit == 9) and thing):
                if thing == False:
                    l.append(1+unit+unitunit)
                else:
                    l.append(unit+unitunit)
                    thing = True
            else:
                if thing == False:
                    l.append(1+unit+unitunit-10)
                else:
                    l.append(unit+unitunit-10)
                    thing = False      
    else:
        for n in range (len(l1)-len(l2)):
            l2.append(0)
        for i in range(len(l1)):
            unit = l1.pop(0)
            unitunit = l2.pop(0)
            if unit + unitunit < 10 and (not (unit + unitunit == 9) and thing):
                if thing == False:
                    l.append(1+unit+unitunit)
                else:
                    l.append(unit+unitunit)
                    thing = True
            else:
                if thing == False:
                    l.append(1+unit+unitunit-10)
                else:
                    l.append(unit+unitunit-10)
                    thing = False 
    if not thing:
        l.append(1)   
    return l

print(addd(l1,l2))
