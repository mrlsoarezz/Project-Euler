import math

n = 600851475143
bigger = 0
def isPrime(number):
    if (number < 2): return False
    for d in range(2, number):
        if (number % d == 0): return False
    return True 

for i in range(2, int(math.sqrt(n) + 1)):
    if isPrime(i):
        if (n % i == 0):
            bigger = i 

print("Biggest factor: ", bigger)



