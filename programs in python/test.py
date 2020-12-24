
def subarrayBitwiseOR(A): 
    res = set() 
    pre = {0} 
    for x in A: 
        pre = {x | y for y in pre} | {x} 
        res |= pre 
    return len(res)
t=int(input())
while t>0:
    t-=1
    n=int(input())
    A=list()
    for x in range(n):
        A.append(int(input().split(sep=" ")))
    for x in range(n):
        print(x,end=" ")
    print(subarrayBitwiseOR(A))