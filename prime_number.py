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
    ''' generate prime numbers up to the limit. 
    This method implements Sieve of Eratosthenes, for a more efficient
    implementation, use the Sieve of Atkin implemented in generatePrimeOpt'''

    # First generate a list of integers from 2 to the limit
    nums = range(2, limit) #TODO use linked list to increase efficiency
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

    found = False

    while not found:
        found = True
        if not n & 1:
            return 2

        for x in range(3, int(n**0.5)+1, 2):
            if n % x == 0:
                n = n/x
                found = False
                break

    return n
