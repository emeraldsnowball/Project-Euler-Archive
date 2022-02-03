import math 

def ispalindrome(arg1):
    return str(arg1) == str(arg1)[::-1]

def largestPalindromeProduct(arg1):

    max = (10**arg1) - 1
    min = 1 + int(max/10)

    maxproduct = 0

    for i in range (max, min -1, -1):
        for j in range(i, min - 1, -1):

            product = i * j

            if (product < maxproduct):
                break
            
            if(ispalindrome(product) and product > maxproduct):
                maxproduct = product



    return maxproduct

print(largestPalindromeProduct(5))