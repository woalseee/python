a = int(input())
b = int(input())
c = int(input())
hap = a + b + c

if hap == 180 :
    if a==b==c==60 :
        print('Equilateral')
    elif a==b!=c:
        print('Isosceles')
    elif a==c!=b:
        print('Isosceles')
    elif b==c!=a:
        print('Isosceles')
    else:
        print('Scalene')
        
else:
    print('Error')