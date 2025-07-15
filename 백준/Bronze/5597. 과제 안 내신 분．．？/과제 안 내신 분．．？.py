num_list = list(range(1,31))

for _ in range(28):
    i = int(input())
    num_list.remove(i)
    
print(min(num_list))
print(max(num_list))