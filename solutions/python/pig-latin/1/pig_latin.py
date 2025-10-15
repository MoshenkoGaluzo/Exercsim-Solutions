def translate_word(text):
    if text.startswith("xr") or text.startswith("yt"):
        return text + "ay"
    test_for = ["a","e","i","o","u","qu","y"]
    new_dict = {text.find(thing):thing for thing in test_for if thing in text}
    min_index = min(new_dict)
    if new_dict[min_index] == "y" and min_index == 0:
        new_dict.pop(min_index)
        min_index = min(new_dict)
    shift_index = text.find(new_dict[min_index])
    if new_dict[min_index] == "qu":
        shift_index += 2
    return text[shift_index:] + text[:shift_index] + "ay"

def translate(text):
    return " ".join([translate_word(word) for word in text.split()])
    
    
