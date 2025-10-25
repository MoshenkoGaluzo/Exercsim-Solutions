def is_valid(isbn):
    isbn = isbn.replace("-","")
    isbn_list = list(isbn)
    if len(isbn_list) != 10:
        return False
    if isbn_list[-1] == "X":
        isbn_list[-1] = "10"

    if not all(ele.isdigit() for ele in isbn_list):
        return False
    
    isbn_list = [int(char) for char in isbn_list]
    return (sum([ num * (10-index) for index, num in enumerate(isbn_list)])) % 11 == 0
