def rotate(text, key):
    
    output = ""
    plain = "abcdefghijklmnopqrstuvwxyz"
    cipher = plain[key:] + plain[:key]
    
    for x in text:
        num = plain.find(x.casefold())
        if(num == -1):
            output = output + x
            continue
        if(x.isupper()):
            output = output + cipher[num].capitalize()
        else:
            output = output + cipher[num]


    return output
