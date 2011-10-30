from prime_number import *

def isPalNum(n, l):
    n1 = str(n)[:l]
    n2 = str(n)[l:]
    for i in range(l):
        if n1[i] != n2[-1-i]:
            return False
    return True

def func(n):
    r = 0
    n1 = n
    while n1>100:
        n2 = n
        while n2>100:
            p = n1*n2
            if r > p:
                break
            if isPalNum(p, 3):
                r = p
            n2 = n2 - 1
        n1 = n1 - 1
    return r
    
if __name__ == '__main__':
    print func(999)
    # print isPalNum(905509, 3)
