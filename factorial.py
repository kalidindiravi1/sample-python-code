def factorial(x):
    num = 1
    while num < x:
        x = x * num
        num += 1
        print num ,
        print x
    
    return x
    
print factorial(4)