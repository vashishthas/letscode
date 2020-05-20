n=int(input("enter the range till the series required:"))
a=0
b=1
while a<=n:
    print(a)
    c=a+b
    a=b
    b=c
