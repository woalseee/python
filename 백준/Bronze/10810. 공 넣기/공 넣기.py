n, m=map(int, input().split())
box = [0]*n

for _ in range(m) :
    i,j,k = map(int, input().split())
    for a in range(i, j+1):
        box[a-1] = k
for i in range(n):
    print(box[i], end=' ')