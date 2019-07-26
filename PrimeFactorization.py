import fileinput
val = 0
for line in fileinput.input():
    val = int(line)

i = 2
vals = []
while i * i <= val:
    if val % i :
        i+=1
    else:
        vals.append(i)
        val //= i
    ## grab the unfactorable
if val > 1:
    vals.append(val)

sorted_vals = reversed(sorted(vals))
print("*".join([str(v) for v in sorted_vals]))