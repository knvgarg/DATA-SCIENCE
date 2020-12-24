# import sys

# sys.stdin = open("input.txt", "r")
# sys.stdout = open("output.txt", "w")
n = int(input())
for x in range(1,n+1): print(x, end=" ")
print()
for x in range(n-1, 0, -1):
    for y in range(x):
        print(y + 1, end=" ")
    print((2*(n-x)-1)*'* ',end="")
    print()

