def max_of_three(a, b, c):
    if a >= b and a >= c:
        print(a)
    else:
        if b >= c:
            print(b)
        else:
            print(c)
