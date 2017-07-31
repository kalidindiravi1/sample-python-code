def product(sequence):
    p = 1
    if sequence == []:
        p = 1
    else:
        for s in sequence:
            p *= s
    return p