n = int(input())

for i in range(n):
    arr = []
    input_arr = list(input())

    for j in input_arr:
        if j == "(" :
            arr.append(j)
    
        elif j == ")":
            if not arr:
                print("NO")
                break
            arr.pop()
    else:
        if not arr:
            print("YES")
        else:
            print("NO")