N, B = input().split()
alpabet_list = list("0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ")
N = N[::-1]
result = 0 

for i,n in enumerate(N):
    result += alpabet_list.index(n)* int(B) ** int(i)
    
print(result)