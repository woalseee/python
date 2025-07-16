word =input().upper()
s = list(set(word))

cnt_list = []
for i in s:
    cnt = word.count(i)
    cnt_list.append(cnt)


if (cnt_list.count(max(cnt_list))) >= 2:
    print('?')
else:
    print(s[cnt_list.index(max(cnt_list))].upper())
    