def count(sequence, item):
    c = 0
    for s in sequence:
        
        if s == item:
            c += 1
    return c
    
    
count([1,2,1,1], 1)