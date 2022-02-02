def fiboEvenSum(arg1):
    maxnum = arg1
    i = 1
    j = 2
    sum = 2

    while i + j < maxnum + 1:
        #print (i)
        temp = i + j
        i = j
        j = temp

        if (j%2 == 0):
            sum += j
    
    #print (j)

    return sum

print (fiboEvenSum(4000000))