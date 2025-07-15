string = input()
alphabet = "abcdefghijklmnopqrstuvwxyz"
arr = []
for i in alphabet:
    arr.append(string.find(i))
print(*arr)