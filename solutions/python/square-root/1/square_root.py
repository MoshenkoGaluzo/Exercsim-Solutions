def square_root(number):
    c = 1
    while abs(number - c**2) >= 1:
        c = -(c**2-number)/(2*c)
    return round(abs(c))
