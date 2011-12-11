def isPrime(n):
    '''check if integer n is a prime
    Note: this method is copied from
    http://www.daniweb.com/software-development/python/code/216880'''

    # make sure n is a positive integer
    n = abs(int(n))

    # 0 and 1 are not primes
    if n < 2:
        return False

    # 2 is the only even prime number
    if n == 2:
        return True

    # all other even numbers are not primes
    if not n & 1:
        return False

    # range starts with 3 and only needs to go up the squareroot of n for all
    # odd numbers
    for x in range(3, int(n**0.5)+1, 2):
        if n % x == 0:
            return False
    return True

def generatePrimes(limit):
    ''' generate prime numbers up to the limit none inclusive. 
    This method implements Sieve of Eratosthenes, for a more efficient
    implementation, use the Sieve of Atkin implemented in generatePrimeOpt'''

    # First generate a list of integers from 2 to the limit
    nums = range(2, limit) # LinkedList would be better, but in pythons case it
                           # worth to implement, since list is in C and self
                           # implemented LinkedList is in python.
    pnums = []

    while len(nums) > 0:
        pnum = nums.pop(0)
        pnums.append(pnum)

        for n in nums:
            if n % pnum == 0:
                nums.remove(n)

    return pnums

def largestPrimeFactor(n):
    ''' Find the largest prime factor of n
    '''

    n = abs(int(n))

    if n < 2:
        return 1

    # if n is even, the largest prime factor is 2
    if not n & 1:
        return 2

    found = False

    while not found:
        found = True
        
        for x in range(3, int(n**0.5)+1, 2):
            if n != x and n % x == 0:
                n = n/x
                found = False
                break

    return n

def getDivisors(n):
    divisors = []

    n = abs(int(n)) # make sure n is a positive integer

    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            d = n/i
            if d != i:
                divisors.append(d)

    return divisors

def getNumDivisors(n):
    """
    A quicker solution for giving the number of divisors without compute the
    actual divisors.

    This algorithm is based on the following property,
    Any integer N can be expressed as follows:
    N = p1**a1 * p2**a2 * p3**a3 * ...
    where 'pn' is a distinc prime number, and 'an' is its exponent.
    E.g. 28 = 2**2 * 7**1

    Furthermore, the number of divisors D(N) of any integer N can be computed
    from: D(N) = (a1 + 1)*(a2 + 1)*(a3 + 1)*...
    'an' being the exponents of the distinct prime numbers which are factors of
    N. E.g. D(28) = (2+1)*(1+1) = 6
    """

    n = abs(int(n))

    r = 1
    i = 2
    while i <= n:
        a = 0
        while n % i == 0:
            n = n / i
            a = a + 1
        r = r * (a + 1)
        i = i + 1

    return r
