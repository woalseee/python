t = int(input())

for i in range(t):
    a,b = input().split()
    a = int(a)

    for j in range(len(b)):
        print(a*b[j],end="")
    print("")