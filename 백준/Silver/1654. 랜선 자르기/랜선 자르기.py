n,k = map(int,input().split())
arr = []
les = 0
largest = 0

for i in range(n):
    tmp = int(input())
    arr.append(tmp)
    arr.sort()
    largest = max(tmp,largest)

lt = 1
rt = largest
cnt = 0 

def count(length):
    cnt = 0
    for x in arr:
        cnt += (x//length)
    return cnt

while lt <= rt:
    mid = (lt+rt)//2
    if count(mid) >= k:
        res = mid
        lt = mid + 1
    else:
        rt = mid - 1

print(res)