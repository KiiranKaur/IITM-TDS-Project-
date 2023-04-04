a=int(input("enter first number:"))
b=int(input("enter second number:"))
c=int(input("enter third number:"))
if a>b and a>c:
    print(a,"is largest")
elif b>c and b>a:
    print(b,"is largest")
elif c>a and c>b:
    print(c,"is largest")
elif a=b=c:
    print("all are equal")
