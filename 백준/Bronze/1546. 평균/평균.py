n = int(input())
arr=list(map(int,input().split()))

num = max(arr)
for i in range(n):
    arr[i] = arr[i]/num*100
print(sum(arr)/len(arr))