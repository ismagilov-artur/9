lozh = False
chisla = int(input())
poisk = []
write = []
for i in range(chisla):
    poisk.append(input())
num1 = int(input())
for i in range(num1):
    write.append(input())
for i in poisk:
    for j in write:
        if j in i:
            lozh = True
        else:
            lozh = False
            break
    if lozh:
        print(i)