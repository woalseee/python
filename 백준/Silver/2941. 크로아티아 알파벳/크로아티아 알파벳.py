c_word = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
n = input()

for i in c_word:
    n = n.replace(i,"*")
print(len(n))