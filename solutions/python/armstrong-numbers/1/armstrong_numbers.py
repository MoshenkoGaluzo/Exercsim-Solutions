def is_armstrong_number(number):
    digits = [int(char)**len(str(number)) for char in str(number)]
    return number == sum(digits)
