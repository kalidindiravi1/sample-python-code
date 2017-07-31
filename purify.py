def purify(sequence):
    even = []
    for s in sequence:
        if s % 2 == 0:
            even.append(s)
    return even
            
            
    


purify([1,2,3,4,5,6,7,8,9,10])