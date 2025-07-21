n,b = input().split()
n = list(n)
n=n[::-1]
b = int(b)

num="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
cnt = 0

for i in range(len(n)):
    cnt = cnt + (num.index(n[i])*(b**i))

print(cnt)