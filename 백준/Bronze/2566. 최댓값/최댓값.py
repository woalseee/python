a=[]
max_list = []
for i in range(9):
    i = list(map(int,input().split()))
    a.append(i)
    
for i in range(9):
    max_list.append(max(a[i]))

max_k = max(max_list)
print(max_k)

for i in range(9):
    for j in range(9):
        if (a[i][j] == max_k):
            print(i+1, j+1, end = ' ')