def remove_duplicates(sequence):
    u = []
    for s in sequence:
        
        if s not in u:
            u.append(s)
    return u
    

remove_duplicates([1,1,2,2,3,4,7,4,3])