def is_pangram(sentence):
    sentence = sentence.lower()
    new_list =[char for char in sentence if char.isalpha()]
    return len(set(new_list)) == 26
    
