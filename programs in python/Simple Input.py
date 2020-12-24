import sys

sys.stdin = open("input.txt", "r")
sys.stdout = open("output.txt", "w")

sum = int(0)
while sum>=0 :
    x=input()
    sum += int(x)
    if sum>=0:
        print(x)

