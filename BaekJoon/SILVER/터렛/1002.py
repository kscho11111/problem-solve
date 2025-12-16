list = []

def ipt():
    num = int(input())
    for i in range (0, num):
        a, b, c, d, e, f = map(int, input().split())
        list.append([a, b, c, d, e, f])

def dist(A, B, C, D):
    return ((C - A)**2 + (D - B)**2)**0.5

if __name__ == "__main__":
    ipt()
    p = len(list)
    #print(list)
    for i in range (0, p):
        a, b, c, d, e, f = list[i]
        dis = dist(a, b, d, e)
        if(a == d and b == e and c == f):
            print(-1)
        elif(c + dis < f or f + dis < c or c +f < dis):
            print(0)
        elif(c + dis == f or f + dis == c or c + f == dis):
            print(1)
        else:
            print(2)