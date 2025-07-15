n,m = map(int,input().split())
arr = []

for i in range(n):
    arr.append(i+1)

for j in range(m):
    a,b = map(int,input().split())
    new_arr = arr[a-1:b]
    new_arr.reverse()
    arr[a-1:b] = new_arr

print(*arr)