import sys
input = sys.stdin.readline

n = int(input())
arr = [ ]

for i in range(n):
    inp = input().split()
    if inp[0] == "1":
        arr.append(inp[1])
    elif inp[0] == "2":
        if len(arr) == 0:
            print(-1)
        else:
            print(arr.pop())
    elif inp[0] == "3":
        print(len(arr))
    elif inp[0] == "4":
        if len(arr) == 0:
            print(1)
        else:
            print(0)
    else:
        if len(arr) == 0:
            print(-1)
        else:
            print(arr[-1])