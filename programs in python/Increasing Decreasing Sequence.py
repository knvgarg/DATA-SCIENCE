import sys
sys.stdin = open('input.txt','r')
sys.stdout = open('output.txt','w')
n = int(input())
a = int(input())
b = int(input())
try:
    while a > b:
        a = b
        b = int(input())
    a = b
    b = int(input())
    while a < b:
        a = b
        b = int(input())
    print("false")
except EOFError:
    print("true")
    pass
