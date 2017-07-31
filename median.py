import math

def median(sequence):
    m = 0
    x = 0.0
    l = len(sequence)
    sequence.sort()
    print sequence
    print l
    if l == 1:
        x = float(sequence[l-1])
        print sequence[l-1], x
    elif l % 2 == 0:
        m = l / 2
        x = (float(sequence[m-1]) + float(sequence[m])) / 2
        print sequence[m-1], sequence[m], x
    else:

        x = sequence[int(math.ceil(l / 2.0) - 1)]
        print sequence, x, m
    return x   
        
median([6, 8, 12, 2, 23])