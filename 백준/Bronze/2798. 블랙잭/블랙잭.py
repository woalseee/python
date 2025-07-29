a, b = map(int,input().split())
arr = list(map(int,input().split()))

result= 0

for i in range(a):
    for j in range(i+1,a):
        for k in range(j+1,a):
            card_sum = arr[i]+arr[j]+arr[k]
            if card_sum <= b:
                result = max(result,card_sum)

print(result)