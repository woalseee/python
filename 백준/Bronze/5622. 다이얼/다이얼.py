s = list(input())
result = []
for i in range(len(s)):

    if (65 <= ord(s[i]) <= 67): #2
        result.append(2)
    elif (68 <= ord(s[i]) <= 70): #3
        result.append(3)
    elif (71 <= ord(s[i]) <= 73): #4
        result.append(4)
    elif (74 <= ord(s[i]) <= 76): #5
        result.append(5)
    elif (77 <= ord(s[i]) <= 79): #6
        result.append(6)
    elif (80 <= ord(s[i]) <= 83): #7
        result.append(7)
    elif (84 <= ord(s[i]) <= 86):#8
        result.append(8)
    elif (87 <= ord(s[i]) <= 90):#9
        result.append(9)

print(sum(result)+len(result))