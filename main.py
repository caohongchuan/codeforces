import sys
input = sys.stdin.readline

############ ---- Input Functions ---- ############
def inp():
    return(int(input()))
def inlt():
    return(list(map(int,input().split())))
def insr():
    s = input()
    return(list(s[:len(s) - 1]))
def invr():
    return(map(int,input().split()))
############ ---- Output Functions ---- ############
def outsr(n):
    sys.stdout.write(str(n) + "\n")
def outlt(nl):
    sys.stdout.write(" ".join(map(str,nl)) + "\n")

even_n = ['2', '4', '6', '8']
num = inp()
for i in range(num):
    str_r = insr()
    if str_r[len(str_r)-1] in even_n:
        outsr(0)
    else:
        if str_r[0] in even_n:
            outsr(1)
        elif len(set(str_r).intersection(set(even_n))) != 0:
            outsr(2)
        else:
            outsr(-1)
