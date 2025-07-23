a,b,c = map(int, input().split())
arr = [a,b,c]

if max(arr) >= sum(arr) - max(arr) :
    print(2*(sum(arr) - max(arr))-1)
else :
    print(sum(arr))