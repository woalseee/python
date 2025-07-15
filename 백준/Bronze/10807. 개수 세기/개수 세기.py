num = int(input())
total_num_list = list(map(int, input().split()))
req = int(input())
number=0

for i in range(0,num):
    if (req == total_num_list[i]):
        number+=1
print(number)