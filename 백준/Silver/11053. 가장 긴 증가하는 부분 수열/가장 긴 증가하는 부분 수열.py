n = int(input())
arr = list(map(int,input().split()))

def lis (arr):
    l = len(arr)
    dp = [1] * l
    for i in range(n):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j]+1)
    return(max(dp))

print(lis(arr))