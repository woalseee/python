a = list(input())
k = []
for i in range(len(a)-1,-1,-1):
    k.append(a[i])

if k == a :
    print(1)
else:
    print(0)