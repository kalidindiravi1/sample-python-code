def digit_sum(n):
    x = str(n)
    total = 0
    for i in x:
        total += int(i)
    return total