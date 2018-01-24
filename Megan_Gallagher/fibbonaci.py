n=1
a=2
b=0
fib=[n,a]
while(n<4000000):
    temp=a
    a=n+temp
    n=temp
    fib.append(a)
for i in fib:
    if (i%2==0):
        b=b+i

print(b)