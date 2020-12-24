import sys

sys.stdin = open("input.txt", "r")
sys.stdout = open("output.txt", "w")
n = int(input())


def fun(n, openn, close, out=[]):
    if close == n:
        print("".join(out))
        return
    else:
        if close < openn:
            out.append(")")
            fun(n, openn, close + 1, out)
            out.pop()
        if openn < n:
            out.append("(")
            fun(n, openn + 1, close, out)
            out.pop()
    return


fun(n, 0, 0)
