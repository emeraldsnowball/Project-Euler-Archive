def sum_mul35(arg1):
    maxnum = arg1
    sum = 0
    for x in range(maxnum):
        if (x % 3 == 0):
            sum += x
            #print(x)
        else:
            if (x%5==0):
                sum += x
                #print(x)
    return sum



print (sum_mul35(1000))
