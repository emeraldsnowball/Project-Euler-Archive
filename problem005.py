import math

def smallestMult(arg1):

    product = 1

    for i in range(1, arg1 + 1):
        product = int((product * i) / math.gcd(product,i))
        
    return (product)

print(smallestMult(10))
