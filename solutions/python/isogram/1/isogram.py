def is_isogram(string):
    lst = list(string.lower())
    while " " in lst:
        lst.remove(" ")
    while "-" in lst:
        lst.remove("-")
    return sum([lst.count(cnt) for cnt in lst]) == len(lst)
