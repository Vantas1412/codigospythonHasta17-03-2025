n1,op1,n2,op2,n3=map(str,input().split())

n1=int(n1)
n2=int(n2)
n3=int(n3)


if op1=="*":
    r1=n1*n2
    if op2=="*":
        r1=r1*n3
    if op2=="-":
        r1=r1-n3
    if op2=="+":
        r1=r1+n3
    
if op2=="*":
    r1=n2*n3
    if op1=="*":
        r1=r1*n1
    if op1=="+":
        r1=r1+n1
    if op1=="-":
        r1=n1-r1
if op1=="+" and op2=="+":
    r1=n1+n2+n3 

if op1=="+" and op2=="-":
    r1=n1+n2-n3 

if op1=="-" and op2=="+":
    r1=n1-n2+n3 

if op1=="-" and op2=="-":
    r1=n1-n2-n3 


print(r1)











