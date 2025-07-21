ip = int(input())
q=0
d=0
n=0
p=0


for i in range(ip):
        m = int(input())
        while m>0:
            if m//25 > 0:
                q = m // 25
                m = m % 25
            elif m//10 >0:
                d = m //10
                m = m%10
            elif m // 5 >0:
                n = m//5
                m = m%5
            elif m //1 >0:
                p = m//1
                m = m%1

        print(q, d, n, p)
        q=d=n=p=0