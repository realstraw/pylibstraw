from prime_number import *
import io
import os

def isPalNum(n, l):
    n1 = str(n)[:l]
    n2 = str(n)[l:]
    for i in range(l):
        if n1[i] != n2[-1-i]:
            return False
    return True

def func():
    for c in range(999, 0, -1):
        for a in range(1, 1000-c):
            b = 1000 - a - c
            if a*a + b*b == c*c:
                return a*b*c

def getMatrix(fileName):
    mat = []
    with io.open(fileName, 'r') as f:
        while True:
            line = f.readline()
            if(len(line) == 0):
                break
            mat.append(line.split())
    return mat

def findMax(mat):
    mx = 0
    
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            h = 1
            v = 1
            d = 1
            dd = 1
            for k in range(4):
                if j + 3 < len(mat):
                    h = h * int(mat[i][j + k])
                if i + 3 < len(mat):
                    v = v * int(mat[i + k][j])
                if j + 3 < len(mat) and i + 3 < len(mat):
                    d = d * int(mat[i + k][j + k])
                if i + 3 < len(mat) and j - 3 >= 0:
                    dd = dd * int(mat[i + k][j - k])

            mx = max(mx, h, v, d, dd)

    return mx


if __name__ == '__main__':        
    mat = getMatrix('mat.txt')
    print findMax(mat)
