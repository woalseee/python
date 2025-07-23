xnum=[]
ynum=[]
for _ in range(3):
    x,y = map(int, input().split())
    xnum.append(x)
    ynum.append(y)

for i in range(3):
    if xnum.count(xnum[i]) == 1:
        xx = xnum[i]
    if ynum.count(ynum[i]) == 1:
        yy = ynum[i]
        
print(xx,yy)