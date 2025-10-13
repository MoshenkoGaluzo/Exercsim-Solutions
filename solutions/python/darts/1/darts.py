def score(x, y):
    dis = x**2 + y**2
    if dis <= 1:
        return 10
    if dis <= 25:
        return 5
    if dis <= 100:
        return 1
    return 0
