a,b = map(int, input().split())
a = list(str(a))
aa = a[2]+ a[1] +a[0]

b = list(str(b))
bb = b[2]+ b[1] +b[0]

if aa>bb:
    print(aa)
else:
    print(bb)