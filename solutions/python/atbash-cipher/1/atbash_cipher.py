plain = "abcdefghijklmnopqrstuvwxyz"
cipher = "zyxwvutsrqponmlkjihgfedcba"

def encode(plain_text):
    text = plain_text.lower().replace(" ", "").replace(",", "").replace(".","")
    enc_text = "".join([plain[cipher.find(char)] if char in cipher else char for char in text])
    final = []
    start = 0
    for i in range(5,len(enc_text),5):
        final.append(enc_text[start:i])
        start += 5
    final.append(enc_text[start:])
    return " ".join(final)


def decode(ciphered_text):
    text = ciphered_text.split()
    dec_text = ""
    for word in text:
        dec_text += "".join([cipher[plain.find(char)] if char in plain else char for char in word])
    return dec_text
