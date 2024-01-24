n = int(input())
right = list()
left = list()
for i in range(n):
    white = input()
    right.append(white)
nn = int(input())
for i in range(nn):
    answer = input()
    left.append(answer)
for i in range(nn):
    if left[i] in right:
        print(left[i])