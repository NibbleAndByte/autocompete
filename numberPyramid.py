import fileinput
pyrSize = 0
for line in fileinput.input():
    pyrSize = int(line)



def getLine(i):
    sent = ''
    for j in range (1,i+1):
        sent += str(j)
    for k in reversed(range (1,i)):
        sent += str(k)
    return sent


for i in range (1,pyrSize+1):
    print (getLine(i))
for i in reversed(range(1,pyrSize)):
    print getLine(i)