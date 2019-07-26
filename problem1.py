import fileinput
sum =  0
for line in fileinput.input():
    sum += int(line)
print(sum)