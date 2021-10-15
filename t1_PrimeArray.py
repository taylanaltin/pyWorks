def IsPrime(n: int) -> bool:
    """This prime found method uses 6k+-1 Method"""
    if n <= 3:
        return n > 1
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i ** 2 <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def NextPrime(N):
    """Finds the next prime number from entered value"""
    if (N <= 1):
        return 2
    prime = N
    found = False
    """Loop continuously until isPrime returns"""
    """True for a number greater than n"""
    while not found:
        prime = prime + 1
        if (IsPrime(prime) == True):
            found = True

    return prime


def PrimeList(n, b, s: int):
    outVal = [0] * n
    outVal[0] = NextPrime(b)
    """First number of the array will be the first nextPrime"""
    for i in range(n - 1):
        for j in range(s + 1):
            """S times prime numbers are not into the list"""
            b = NextPrime(b) + 1
        outVal[i + 1] = NextPrime(b)
        """ This enters the prime numbers to array list"""
    return outVal


def MirrorList(inlist):
    sum = 0
    for i in range(0, len(inlist)):
        sum = sum + inlist[i]
        stringsum = str(sum)
    return int(stringsum[::-1])


"""User input for n,b,s"""
b = int(input("Enter the B \n"))
n = int(input("Enter the N \n"))
s = int(input("Enter the S \n"))
out = PrimeList(n, b, s)
print(out)
print(MirrorList(out))
input()
"""For stop the program"""
