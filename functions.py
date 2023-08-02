def max(*args):
    max=0
    for el in args:
        if el > max:
           max = el

    return max



print(max(10,5, 20,14))
