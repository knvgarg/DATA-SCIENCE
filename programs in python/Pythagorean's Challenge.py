# import sys
# sys.stdin = open('input.txt','r')
# sys.stdout = open('output.txt','w')
t=1
while t>0:
    t-=1
    a=25
    tup=0,int(a**0.5)
    print(tup,sep=" ")
    for x in range(int(a**0.5)-1,0,-1):
        var= float(a-x**2)
        if var.is_integer():
            print(var,x)
