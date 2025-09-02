n = int(input())
arr = [ ]

for i in range(n):
    k = int(input())
    if k != 0:
        arr.append(k)
    else:
        arr.pop()

res = 0

for k in arr:
    res = res+k
print(res)