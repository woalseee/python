n = int(input())
arr = []

for i in range(n):
    arr.append(list(map(int, input().split())))

x = []
y = []
for i in range(len(arr)):
    x.append(arr[i][0])
for j in range(len(arr)):
    y.append(arr[j][1])

if len(arr) == 1:
    print(0)
else:
    print((max(x)-min(x))*(max(y)-min(y)))