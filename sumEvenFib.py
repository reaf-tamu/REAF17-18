import math

fiblist = []
x1 = 1
x2 = 2
fiblist.append(x1)
fiblist.append(x2)
while (x1 < 4000000):
    new = x1 + x2
    fiblist.append(new)
    x1 = x2
    x2 = new
evensum = 0
for i in fiblist:
    if(i%2 == 0):
        evensum = evensum + i

print(evensum)
