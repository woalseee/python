a,b,c = map(int,input().split())

if a==b==c:
    print(10000+a*1000)
elif a==b or b==c:
    print(1000+100*b)
elif c==a:
    print(1000+100*c)
else:
    list=[a,b,c]
    s=max(list)
    print(100*s)