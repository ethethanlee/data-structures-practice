# so somehow need to come up with a center and then determine distance from that center for each point
# 2.333, 4.5

# -3, 0 to 7, 9 - do every point? eventually theyd get to 0 4

# distance formula is like sqrt difference in x squared + difference in y squared

darts = [[-3,0],[3,0],[2,6],[5,4],[0,9],[7,8]]
r = 5



def numPoints(darts, r):
    lx = 0
    gx = 0
    ly = 0
    gy = 0
    total = 0
    for value in darts:
        if value[0] < lx:
            lx = value[0]
        if value[0] > gx:
            gx = value[0]
        if value[1] < ly:
            ly = value[1]
        if value[1] > gy:
            gy = value[1]
    for i in range(lx,gx):
        for n in range(ly,gy):
            counter = 0
            for value in darts:
                if ((i-value[0])*(i-value[0]) + (n-value[1])*(n-value[1])) <= (r*r):
                    counter = counter + 1
            if total < counter:
                total = counter
    return total


print(numPoints(darts, r))