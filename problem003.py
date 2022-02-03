import math

def largestPrimeFactor(arg1):
    n = arg1

    maxprime = 1

    if n % 2 == 0:
      maxprime = 2
      return maxprime
    
    for i in range(3, int(math.sqrt(n)) + 1, 2):
      if n % i == 0:
         maxprime = i
         n = n / i
    return int(maxprime)

print(largestPrimeFactor(13195))
